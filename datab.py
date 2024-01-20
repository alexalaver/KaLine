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