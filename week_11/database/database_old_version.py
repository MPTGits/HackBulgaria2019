import os
import sqlite3
from utils.constant_variables import *


class Database:

    #Creating all the tables in the database 

    @classmethod
    def creat_tables(cls):
        conn = sqlite3.connect(DatabaseConstants.MAIN_DATABASE_NAME)
        c=conn.cursor()
        
        c.execute(
            """CREATE TABLE IF NOT EXISTS User
                 (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                    username VARCHAR(255) NOT NULL UNIQUE, 
                    hashed_password VARCHAR(255) NOT NULL,
                    status VARCHAR(255) NOT NULL""")

        c.execute(
            """CREATE TABLE IF NOT EXISTS Doctor
            (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            userID INTEGER FOREIGN KEY REFERENCES User(id),
            title VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL,
            age INTEGER,
            doctor_schedulID INTEGER
            """)

        c.execute(
            """CREATE TABLE IF NOT EXISTS Patient
                (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                userID INTEGER FOREIGN KEY REFERENCES User(id),
                name VARCHAR(255) NOT NULL UNIQUE, 
                age INTEGER,
                patient_schedulID INTEGER""")

        c.execute(
            """CREATE TABLE IF NOT EXISTS Schedule
                (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                doctorID INTEGER FOREIGN KEY REFERENCES Doctor(id) NOT NULL,
                date DATE NOT NULL, 
                userID INTEGER FOREIGN KEY REFERENCES Doctor(id) NOT NULL,
                """)

    @classmethod
    def add_user(cls,username,hashed_password,stauts=None):
    conn = sqlite3.connect(DatabaseConstants.MAIN_DATABASE_NAME)
    c=conn.cursor() 
    c.execute("""INSERT INTO User (username,hashed_password,status) VALUES (%s, %s, %s)""", (username,hashed_password,status))

    if status:
        c.execute("""INSERT INTO %s (username,hashed_password,status) VALUES (%s, %s,%s,%s)""", (status,))

    conn.commit()
    conn.close()



