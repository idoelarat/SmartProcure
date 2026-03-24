# test_db.py
import unittest
from database import engine, SessionLocal
from models import Base, Part, Category, Stock


class TestBase(unittest.TestCase):
    def setUp(self):
        # Create tables only if they don't exist
        Base.metadata.create_all(bind=engine)
        self.db = SessionLocal()

    def tearDown(self):
        self.db.close()

class TestCategory(TestBase):
    def test_create_category(self):
        # Check if "Electronics" already exists
        cat = self.db.query(Category).filter_by(name="Electronics").first()
        if not cat:
            cat = Category(name="Electronics")
            self.db.add(cat)
            self.db.commit()
        
        self.assertGreaterEqual(self.db.query(Category).count(), 1)

class TestParts(TestBase):
    def test_part_linking_to_category(self):
        # Get or Create Category
        cat = self.db.query(Category).filter_by(name="Hardware").first()
        if not cat:
            cat = Category(name="Hardware")
            self.db.add(cat)
            self.db.commit()

        # Check if Part "P1" already exists
        p = self.db.query(Part).filter_by(sku="P1").first()
        if not p:
            p = Part(sku="P1", name="Nut", category_id=cat.id)
            self.db.add(p)
            self.db.commit()
        
        self.assertEqual(p.category.name, "Hardware")

class TestStock(TestBase):
    def test_stock_initialization(self):
        # Get or create the necessary setup
        cat = self.db.query(Category).filter_by(name="General").first()
        if not cat:
            cat = Category(name="General")
            self.db.add(cat)
            self.db.commit()

        p = self.db.query(Part).filter_by(sku="S1").first()
        if not p:
            p = Part(sku="S1", name="Bolt", category=cat)
            self.db.add(p)
            self.db.flush() # Get the ID without committing yet

        # Check if Stock exists for this part
        s = self.db.query(Stock).filter_by(part_id=p.id).first()
        if not s:
            s = Stock(quantity=100, part=p)
            self.db.add(s)
            self.db.commit()

        self.assertEqual(p.stock.quantity, 100)

if __name__ == "__main__":
    unittest.main(verbosity=2)
