import os
import sqlite3

def creat_user_table(database_name):
    conn = sqlite3.connect(database_name)
    c=conn.cursor()
    if os.path.exists(database_name): 
        c.execute(
            """CREATE TABLE User
                 (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, full_name VARCHAR(255) NOT NULL UNIQUE, email VARCHAR(255) NOT NULL UNIQUE, age int NOT NULL, phone VARCHAR(255) NOT NUll,aditional_info text)""")
    conn.commit()
    conn.close()

#creat_user_table('vizitka.db')
    
def add(database_name):
    full_name=input("Enter user name:")
    email=input("Enter user email:")
    age=input("Enter user age:")
    phone=input("Enter user phone:")
    aditional_info=input("Enter user aditional_info:")

    conn = sqlite3.connect(database_name)
    c=conn.cursor() 
    c.execute("""
        INSERT INTO User
        (full_name,email,age,phone,aditional_info)
            VALUES (
            '{full_name}',
            '{email}',
            '{age}',
            '{phone}',
            '{aditional_info}'
            )
            """.format(full_name=full_name,email=email,age=age,phone=phone,aditional_info=aditional_info))
    conn.commit()
    conn.close()

#add('vizitka.db','Marto','e',20,'088PapiHans','Sansa umira')
#add('vizitka.db','Martov2.0','b',21,'088PapiHan','Ghost umira')

def list_users(database_name):
    conn = sqlite3.connect(database_name)
    c=conn.cursor() 
    c.execute("SELECT id, full_name,email,age,phone,aditional_info FROM User")
    users = c.fetchall()

    conn.commit()

    conn.close()

    return users


#print(list_users('vizitka.db'))


def get(database_name):
    desiered_id=input("Input id of an user to get:")
    conn = sqlite3.connect(database_name)
    c=conn.cursor() 
    c.execute("SELECT id, full_name,email,age,phone,aditional_info FROM User WHERE id='{desiered_id}'".format(desiered_id=desiered_id))
    user = c.fetchone()

    conn.commit()

    conn.close()

    return user

#print(get('vizitka.db',3))
    

def delete(database_name):
    desiered_id=input("Input id of an user to delete:")
    conn = sqlite3.connect(database_name)
    c=conn.cursor() 
    c.execute("DELETE  FROM User WHERE id='{desiered_id}'".format(desiered_id=desiered_id))

    conn.commit()

    conn.close()

    print("Deletion was successful!")




def help_opt():
    print("""

            ||||||||||||||||||||||||||||||
            |||||||||||||HELP|||||||||||||
            ||||||||||||||||||||||||||||||

            1.'add'-Add a new buisness card
            2.'list'-List all of the business cards
            3.'delete'-Delet a buisiness card
            4.'get'-Get an buisness card with id""")

