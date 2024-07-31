class RandomFact:
    
    def __init__(self, user_id: int, fact_id: str, date: str, text: str, source: str):
        self.user_id = user_id
        self.fact_id = fact_id
        self.date = date
        self.text = text
        self.source = source
        
    def __str__(self):
        return f"RandomFact(user_id={self.user_id}, fact_id={self.fact_id}, date={self.date}, text={self.text}, source={self.source})"

