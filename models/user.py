class User:

    def __init__(self, id: int, name: str, username: str):
        self.id = id
        self.name = name
        self.username = username

    def __str__(self):
        return f'"name": "{self.name}", "username": "{self.username}"'