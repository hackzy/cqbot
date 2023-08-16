import sqlite3
class Commad:
    commad = []
    def __init__(self) -> None:
        self.connect = sqlite3.connect(database='data/cqbot.db')
        self.cur = self.connect.cursor()
    def createDB(self):
        sql = """CREATE TABLE black(
        commad INT PRIMARY KEY     NOT NULL,
        func text not null
        )"""
        self.cur.execute(sql)
    
