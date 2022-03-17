class User:
    PASSWORD = ""
    def __init__(self, name : str):
        self.name = name
    @classmethod
    def set_password(cls, password : str):
        cls.PASSWORD = password
