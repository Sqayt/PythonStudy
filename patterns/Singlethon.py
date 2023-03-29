class DataBase:
    __instance = None

    def __call__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"connect with DB: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("close connect to DB")

    def read(self):
        return "data for database"

    def write(self, data):
        print(f"Write to DB {data}")


if __name__ == '__main__':
    db = DataBase('root', '1234', 80)
    db2 = DataBase('root2', '5678', 8080)
    print(id(db), id(db2), id(db) == id(db2))

    db.connect()
    db2.connect()
