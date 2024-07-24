import sqlite3
from models.user import User

class UserDAO:
    def __init__(self):
        self.db_path = "/db/random_db.db"
        
    def get_user_by_username(self, username: str) -> User:
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        cur.execute('SELECT id, name, username FROM users WHERE username = ?', (username,))
        row = cur.fetchone()
        if row is not None:
            user = User(row[0], row[1], row[2])
            con.close()
            return user
        else:
            con.close()
            return None
        
    def get_by_id(self, id: int) -> User:
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        cur.execute('SELECT id, name, username FROM users WHERE id = ?', (id,))
        row = cur.fetchone()
        if row is not None:
            user = User(row[0], row[1], row[2])
            con.close()
            return user
        else:
            con.close()
            return None
        
    def create_user(self, user):
        try:
            with sqlite3.connect(self.db_path) as con:
                cur = con.cursor()
                cur.execute('INSERT INTO users (name, username) VALUES (?, ?) RETURNING id;', (user.name, user.username,))
                user_id = cur.fetchone()[0]
                con.commit()
                return user_id
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            return False