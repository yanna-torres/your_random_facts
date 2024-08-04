import sqlite3
from models.fact import RandomFact

class FactDAO:

    def __init__(self):
        self.db_path = "db/random_db.db"
        
    def save_fact(self, fact: RandomFact):
        try:
            con = sqlite3.connect(self.db_path)
            cur = con.cursor()
            cur.execute('INSERT INTO facts (user_id, fact_id, date, text, source) VALUES (?, ?, ?, ?, ?);', (fact.user_id, fact.fact_id, fact.date, fact.text, fact.source))
            con.commit()
            con.close()
            return True
        except Exception as e:
            print(e)
            return False
        
    def get_facts_by_user(self, user_id: int) -> list[RandomFact]:
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        cur.execute('SELECT fact_id, date, text, source FROM facts WHERE user_id = ?;', (user_id,))
        rows = cur.fetchall()
        facts = []
        for row in rows:
            fact = RandomFact(user_id, row[0], row[1], row[2], row[3])
            facts.append(fact)
        con.close()
        return facts
    
    def delete_fact(self, fact_id: int, user_id: int) -> bool:
        try:
            con = sqlite3.connect(self.db_path)
            cur = con.cursor()
            cur.execute('DELETE FROM facts WHERE fact_id = ? AND user_id = ?;', (fact_id, user_id))
            con.commit()
            con.close()
            return True
        except Exception as e:
            print(e)
            return False
