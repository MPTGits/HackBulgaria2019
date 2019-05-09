
def creat_table(table_name,database_name='vehicle_management.db'):
    conn = sqlite3.connect(database_name)
    c=conn.cursor()
    if not os.path.exists(database_name): 
        c.execute(
            """CREATE TABLE '{table_name}'
                 (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                 full_name VARCHAR(255) NOT NULL UNIQUE, 
                 email VARCHAR(255) NOT NULL UNIQUE, 
                 phone VARCHAR(255) NOT NUll,
                 address text)""".format(table_name=table_name))
    conn.commit()
    conn.close()

creat_table('BaseUser')
creat_table('Client')
creat_table('Mechanic')
creat_table('Vehicle')
creat_table('Service')
creat_table('Mechanic_services')
creat_table('Vehicle_repair')
