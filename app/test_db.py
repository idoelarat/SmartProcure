# test_db.py
import unittest
from sqlalchemy.exc import IntegrityError
from database import engine, SessionLocal
from models import Base, Part, Category


class TestInventory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base.metadata.create_all(bind=engine)

    def setUp(self):
        self.db = SessionLocal()
        self.cat = self.db.query(Category).filter_by(name="General").first()
        if not self.cat:
            self.cat = Category(name="General")
            self.db.add(self.cat)
            self.db.commit()

    def tearDown(self):
        self.db.close()

    def test_create_part(self):
        """Adds a part. You can see this in your DB browser after!"""
        p = Part(sku="P1", name="Nut", category_id=self.cat.id)
        self.db.add(p)
        try:
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            print("\n[INFO] SKU 'P1' already exists, skipping insert.")

    def test_count_data(self):
        """Simple check to see how many items you've accumulated."""
        count = self.db.query(Part).count()
        print(f"\n[INFO] Total parts currently in DB: {count}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
