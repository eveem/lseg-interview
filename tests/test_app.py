import unittest
from app.app import app

class AppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_homepage(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_cycle_dogs(self):
        response = self.app.get("/")
        self.assertIn(b"lunar.jpg", response.data)

        response = self.app.get("/")
        self.assertIn(b"solar.jpg", response.data)

        response = self.app.get("/")
        self.assertIn(b"stellar.jpg", response.data)

        response = self.app.get("/")
        self.assertIn(b"next-dog.png", response.data)

        response = self.app.get("/")
        self.assertIn(b"lunar.jpg", response.data)

if __name__ == "__main__":
    unittest.main()