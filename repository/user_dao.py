import sqlite3
from models.user import User

class UserDAO:
    def __init__(self):
        self.db_path = "db/random_db.db"
        
    def get_user_by_username(self, username: str) -> User:
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        cur.execute('SELECT id, name, username FROM users WHERE username = %s', (username,))
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
        cur.execute('SELECT id, name, username FROM users WHERE id = %s', (id,))
        row = cur.fetchone()
        if row is not None:
            user = User(row[0], row[1], row[2])
            con.close()
            return user
        else:
            con.close()
            return None
        
    def create_user(self, user: User):
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        cur.execute('INSERT INTO users (name, username) VALUES (%s, %s) RETURNING id;', (user.name, user.username,))
        con.commit()
        user_id = cur.lastrowid
        con.close()
        return self.get_one(user_id)