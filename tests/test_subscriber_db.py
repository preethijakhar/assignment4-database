import mysql.connector
import unittest

class TestSubscribers(unittest.TestCase):
    def setUp(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="pass",
            database="subscribersdb"
        )
        self.cursor = self.conn.cursor()

    def tearDown(self):
        self.conn.close()

    def test_create_subscriber(self):
        self.cursor.execute("INSERT INTO subscribers (name, email) VALUES ('Test User', 'test@example.com')")
        self.conn.commit()
        self.cursor.execute("SELECT * FROM subscribers WHERE email='test@example.com'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)

    def test_read_subscribers(self):
        self.cursor.execute("SELECT * FROM subscribers")
        result = self.cursor.fetchall()
        self.assertIsInstance(result, list)

    def test_update_subscriber(self):
        self.cursor.execute("UPDATE subscribers SET name='Updated User' WHERE email='test@example.com'")
        self.conn.commit()
        self.cursor.execute("SELECT name FROM subscribers WHERE email='test@example.com'")
        self.assertEqual(self.cursor.fetchone()[0], 'Updated User')

    def test_delete_subscriber(self):
        self.cursor.execute("DELETE FROM subscribers WHERE email='test@example.com'")
        self.conn.commit()
        self.cursor.execute("SELECT * FROM subscribers WHERE email='test@example.com'")
        self.assertIsNone(self.cursor.fetchone())
