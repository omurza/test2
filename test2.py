
import sqlite3
class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self
    def  uzas(self):
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()  
            print("лавочка открыта")
    def uzas1(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None
            print(f"лавочка прикрыта")
    def nohodka(self, username):
            self.uzas()
            self.cursor.execute("SELECT * FROM users WHERE VALUES (?)", (username,))
            res = self.cursor.fetchone()
            self.uzas1()
            return f' ужас я лишился 90 процентов нервов пока искал источник проблемы -{res}'
    def nerd(self, dumbs):
            self.uzas()
            self.conn.execute('BEGIN TRANSACTION')
            for dumb in dumbs:
                self.cursor.execute(dumb)
            self.conn.commit()


class User:
    def __init__(self, db_manager):
        self.db_manager = db_manager
    def add_user(self, user_id, username, email , ):
        self.db_manager.uzas()
        self.db_manager.cursor.execute("INSERT INTO users (id, username, email) VALUES (?, ?, ?)", (user_id, username, email))
        self.db_manager.uzas1()
    def id(self, user_id):
        self.db_manager.uzas()
        self.db_manager.cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        result = self.db_manager.cursor.fetchone()
        self.db_manager.uzas1()
        return f" ну пон{result}"
    def delet(self, user_id):
        self.db_manager.uzas()
        self.db_manager.cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
        self.db_manager.uzas1()
class Admin(User):
    def __init__(self, db_manager):
        super().__init__(db_manager)

    def admin(self, admin_id, username, email, permissions):
        self.db_manager.uzas()
        self.db_manager.cursor.execute("INSERT INTO admins (id, username, email, permissions) VALUES (?, ?, ?, ?)", (admin_id, username, email, permissions))
        self.db_manager.uzas1()

class Customer(User):
    def __init__(self, db_manager):
        super().__init__(db_manager)

    def add_customer(self, customer_id, username, email, address):
        self.db_manager.uzas()
        self.db_manager.cursor.execute("INSERT INTO customers (id, username, email, address) VALUES (?, ?, ?, ?)", (customer_id, username, email, address))
        self.db_manager.uzas1()


if __name__ == "__main__":
    db_manager = DatabaseManager('my_database.db')
    db_manager.uzas()
    db_manager.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                    id INTEGER PRIMARY KEY,
                                    username TEXT NOT NULL,
                                    email TEXT NOT NULL
                                )''')
    db_manager.cursor.execute('''CREATE TABLE IF NOT EXISTS admins (
                                    id INTEGER PRIMARY KEY,
                                    username TEXT NOT NULL,
                                    email TEXT NOT NULL,
                                    permissions TEXT
                                )''')
    db_manager.cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                                    id INTEGER PRIMARY KEY,
                                    username TEXT NOT NULL,
                                    email TEXT NOT NULL,
                                    address TEXT
                                )''')
    db_manager.uzas1()

    user_manager = User(db_manager)
    admin_manager = Admin(db_manager)
    customer_manager = Customer(db_manager)

    user_manager.add_user(1, 'johndoe', 'johndoe@example.com')
    print(user_manager.id(1))
    user_manager.delet(1)

    admin_manager.admin(1, 'admin1', 'admin1@example.com', 'full_access')
    customer_manager.add_customer(1, 'customer1', 'customer1@example.com', '123 Main St')
    queries = [
        "INSERT INTO users (id, username, email) VALUES (2, 'janedoe', 'janedoe@example.com')",
        "INSERT INTO admins (id, username, email, permissions) VALUES (2, 'admin2', 'admin2@example.com', 'limited_access')"
    ]
   


























































