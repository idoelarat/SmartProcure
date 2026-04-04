# scripts\faker_data.py
import random
from faker import Faker
from app.database import SessionLocal, engine
from app.models import Base, Part, Category, Stock, Supplier, Customer, StockMovement

fake = Faker()


def populate_data():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        categories = []
        category_names = [
            "Electronics",
            "Hardware",
            "Tools",
            "Safety Gear",
            "Fasteners",
        ]
        for name in category_names:
            cat = Category(name=name)
            db.add(cat)
            categories.append(cat)
        db.flush()

        suppliers = [
            Supplier(name=fake.company(), contact_info=fake.email()) for _ in range(120)
        ]
        customers = [Customer(name=fake.name()) for _ in range(250)]
        db.add_all(suppliers + customers)
        db.flush()

        parts = []
        for _ in range(1350):
            part = Part(
                sku=fake.unique.bothify(text="??-#####"),
                vendor_sku=fake.bothify(text="VND-####"),
                name=fake.catch_phrase(),
                description=fake.sentence(),
                category=random.choice(categories),
            )
            db.add(part)
            parts.append(part)

            stock = Stock(part=part, quantity=random.randint(10, 100))
            db.add(stock)

        db.flush()

        for _ in range(350):
            m_type = random.choice(["incoming", "outgoing"])
            part = random.choice(parts)
            qty = random.randint(1, 20)

            movement = StockMovement(
                part=part,
                quantity=qty if m_type == "incoming" else -qty,
                movement_type=m_type,
                supplier=random.choice(suppliers) if m_type == "incoming" else None,
                customer=random.choice(customers) if m_type == "outgoing" else None,
                note=fake.sentence(),
            )
            db.add(movement)

        db.commit()
        print("Database successfully populated!")

    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    populate_data()
