import os, uuid, unittest
import mysql.connector as mysql

DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = int(os.getenv("DB_PORT", "3307"))  # 3307 locally via compose
DB_NAME = os.getenv("DB_NAME", "subscribersdb")
DB_USER = os.getenv("DB_USER", "subuser")
DB_PASS = os.getenv("DB_PASS", "subpass")

class TestSubscribers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = mysql.connect(
            host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASS
        )
        cls.conn.autocommit = True

    @classmethod
    def tearDownClass(cls):
        try: cls.conn.close()
        except: pass

    def test_create_read_update_delete(self):
        email = f"u_{uuid.uuid4().hex[:12]}@ex.com"
        with self.conn.cursor() as cur:
            # CREATE
            cur.execute("INSERT INTO subscribers (name, email) VALUES (%s, %s)", ("Preethi", email))
            # READ
            cur.execute("SELECT name FROM subscribers WHERE email=%s", (email,))
            self.assertEqual(cur.fetchone()[0], "Preethi")
            # UPDATE
            cur.execute("UPDATE subscribers SET name=%s WHERE email=%s", ("Updated", email))
            cur.execute("SELECT name FROM subscribers WHERE email=%s", (email,))
            self.assertEqual(cur.fetchone()[0], "Updated")
            # DELETE
            cur.execute("DELETE FROM subscribers WHERE email=%s", (email,))
            cur.execute("SELECT id FROM subscribers WHERE email=%s", (email,))
            self.assertIsNone(cur.fetchone())

if __name__ == "__main__":
    unittest.main()
