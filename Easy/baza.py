import mysql.connector

class DatabaseNB:
    def __init__(self) -> None:
        
        self.ConnectDB()
        self.CreateDB()
        self.CreateTB()

    def ConnectDB(self):
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ravshanbek2003"
        )
        self.cursor=self.conn.cursor()

    def CreateDB(self):
        sql="create database if not exists nb;"
        self.cursor.execute(sql)
        sql="use nb;"
        self.cursor.execute(sql)

    def CreateTB(self):
        
        sql="""create table if not exists tableNB 
        (id serial, lesson varchar(64), student_id int, nb boolean);"""
        self.cursor.execute(sql)

    def Insert(self, lesson, student_id, nb):
        sql=f"insert into tableNB(lesson, student_id, nb) values('{lesson}', {student_id}, {nb});"
        self.cursor.execute(sql)
        self.conn.commit()

db=DatabaseNB()
db.Insert("1-dars", 1, True)
db.Insert("1-dars", 2, True)
db.Insert("1-dars", 3, False)
db.Insert("1-dars", 4, True)
db.Insert("1-dars", 5, False)
db.Insert("1-dars", 6, True)