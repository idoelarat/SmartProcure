# test_db.py
import unittest
from database import engine, SessionLocal
from models import Base, Part, Category, Stock, Supplier, Customer, StockMovement


class TestBase(unittest.TestCase):
    def setUp(self):
        Base.metadata.create_all(bind=engine)
        self.db = SessionLocal()

    def tearDown(self):
        self.db.close()


class TestCategory(TestBase):
    def test_create_category(self):
        cat = self.db.query(Category).filter_by(name="Electronics").first()
        if not cat:
            cat = Category(name="Electronics")
            self.db.add(cat)
            self.db.commit()

        self.assertGreaterEqual(self.db.query(Category).count(), 1)


class TestParts(TestBase):
    def test_part_linking_to_category(self):
        cat = self.db.query(Category).filter_by(name="Hardware").first()
        if not cat:
            cat = Category(name="Hardware")
            self.db.add(cat)
            self.db.commit()

        p = self.db.query(Part).filter_by(sku="P1").first()
        if not p:
            p = Part(sku="P1", name="Nut", category_id=cat.id)
            self.db.add(p)
            self.db.commit()

        self.assertEqual(p.category.name, "Hardware")


class TestStock(TestBase):
    def test_stock_initialization(self):
        cat = self.db.query(Category).filter_by(name="General").first()
        if not cat:
            cat = Category(name="General")
            self.db.add(cat)
            self.db.commit()

        p = self.db.query(Part).filter_by(sku="S1").first()
        if not p:
            p = Part(sku="S1", name="Bolt", category=cat)
            self.db.add(p)
            self.db.flush()

        s = self.db.query(Stock).filter_by(part_id=p.id).first()
        if not s:
            s = Stock(quantity=100, part=p)
            self.db.add(s)
            self.db.commit()

        self.assertEqual(p.stock.quantity, 100)


class TestSupliers(TestBase):
    def test_create_supplier(self):
        s_name = "Global Parts Inc"
        supplier = self.db.query(Supplier).filter_by(name=s_name).first()
        if not supplier:
            supplier = Supplier(name=s_name, contact_info="supply@global.com")
            self.db.add(supplier)
            self.db.commit()

        self.assertIsNotNone(supplier.id)
        self.assertEqual(supplier.name, s_name)


class TestCustomers(TestBase):
    def test_create_customer(self):
        c_name = "Israeli Aircraft Industries"
        customer = self.db.query(Customer).filter_by(name=c_name).first()
        if not customer:
            customer = Customer(name=c_name)
            self.db.add(customer)
            self.db.commit()

        self.assertIsNotNone(customer.id)
        self.assertEqual(customer.name, c_name)


class TestStockMovments(TestBase):
    def test_incoming_shipment_from_supplier(self):
        cat = self.db.query(Category).first() or Category(name="General")
        self.db.add(cat)
        self.db.flush()

        part = self.db.query(Part).filter_by(sku="MOV-1").first()
        if not part:
            part = Part(sku="MOV-1", name="Engine Valve", category=cat)
            self.db.add(part)

        supp = self.db.query(Supplier).first() or Supplier(name="Test Supp")
        self.db.add(supp)
        self.db.flush()

        movement = StockMovement(
            part=part,
            quantity=50,
            movement_type="incoming",
            supplier=supp,
            note="Monthly supply",
        )
        self.db.add(movement)
        self.db.commit()

        self.assertIn(movement, part.movements)
        self.assertEqual(movement.supplier.name, supp.name)
        self.assertIn(movement, supp.movements)

    def test_outgoing_shipment_to_customer(self):
        cat = self.db.query(Category).first() or Category(name="General")
        part = self.db.query(Part).first()
        if not part:
            part = Part(sku="P2", name="Gear", category=cat)
            self.db.add(part)

        cust = self.db.query(Customer).first() or Customer(name="Test Cust")
        self.db.add(cust)
        self.db.flush()

        movement = StockMovement(
            part=part, quantity=-10, movement_type="outgoing", customer=cust
        )
        self.db.add(movement)
        self.db.commit()

        self.assertEqual(movement.customer.name, cust.name)
        self.assertIn(movement, cust.movements)


if __name__ == "__main__":
    unittest.main(verbosity=2)
