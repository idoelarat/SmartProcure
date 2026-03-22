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

    def test_create_and_count(self):
        p = Part(sku="P1", name="Nut", category_id=self.cat.id)
        self.db.add(p)
        self.db.commit()

        count = self.db.query(Part).count()
        print(f"\n[INFO] Total parts after insert: {count}")
        self.assertGreater(count, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
