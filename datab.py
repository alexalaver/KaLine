import psycopg2

class Data:
    def __init__(self, host1, port1, data, user1, password1):
        self.connect = psycopg2.connect(
            host=host1,
            port=port1,
            database=data,
            user=user1,
            password=password1
        )
        self.cursor = self.connect.cursor()

    def add_user(self, id, user_id, first_name, username, lang):
        with self.connect:
            self.cursor.execute("INSERT INTO users(id, user_id, first_name, username, lang) VALUES(%s, %s, %s, %s, %s)", (id, user_id, first_name, username, lang,))
            self.connect.commit()

    def check_user(self, user_id):
        with self.connect:
            self.cursor.execute("SELECT user_id FROM users WHERE user_id=%s", (user_id,))
            return bool(len(self.cursor.fetchall()))

    def check_numbers_id(self):
        with self.connect:
            self.cursor.execute("SELECT id FROM users ORDER BY id DESC LIMIT 1;")
            a = self.cursor.fetchone()
            if a is None:
                return 0
            else:
                return a[0]

    def select_language(self, user_id):
        with self.connect:
            self.cursor.execute("SELECT lang FROM users WHERE user_id=%s", (user_id,))
            a = self.cursor.fetchone()[0]
            return a

    def select_orders_all_new(self):
        with self.connect:
            self.cursor.execute("SELECT orders_new FROM orders_all")
            a = self.cursor.fetchone()[0]
            if a is None:
                return []
            else:
                return a

    def select_orders_all_used(self):
        with self.connect:
            self.cursor.execute("SELECT orders_used FROM orders_all")
            a = self.cursor.fetchone()[0]
            if a is None:
                return []
            else:
                return a

    def update_orders_all_new(self, new):
        with self.connect:
            self.cursor.execute("UPDATE orders_all SET orders_new=%s", (new,))
            self.connect.commit()

    def update_orders_all_used(self, new):
        with self.connect:
            self.cursor.execute("UPDATE orders_all SET orders_used=%s", (new,))
            self.connect.commit()

    def select_orders_user(self, user_id):
        with self.connect:
            self.cursor.execute("SELECT orders FROM users WHERE user_id=%s", (user_id,))
            a = self.cursor.fetchone()[0]
            if a is None:
                return []
            else:
                return a

    def update_orders_user(self, user_id, new):
        with self.connect:
            self.cursor.execute("UPDATE users SET orders=%s WHERE user_id=%s", (new, user_id))
            self.connect.commit()