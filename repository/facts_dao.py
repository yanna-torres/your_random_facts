import sqlite3
from models.fact import RandomFact

class FactDAO:

    def __init__(self):
        self.db_path = "db/random_db.db"
        
    def save_fact(self, fact: RandomFact):
        try:
            con = sqlite3.connect(self.db_path)
            cur = con.cursor()
            cur.execute('INSERT INTO facts (user_id, fact_id, date, text, source) VALUES (%s, %s, %s, %s, %s);', (fact.user_id, fact.fact_id, fact.date, fact.text, fact.source))
            con.commit()
            con.close()
            return True
        except Exception as e:
            print(e)
            return False