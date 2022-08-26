import sqlite3


class DbContext:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor_name = self.conn.cursor()

    def execute_query(self, sql_query: str):
        self.cursor_name.execute(sql_query)
        self.save()

    def save(self):
        self.conn.commit()

    def close(self):
        self.conn.close()
