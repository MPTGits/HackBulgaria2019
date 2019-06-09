#Just messing around with some stuff

# from sqlalchemy import create_engine,MetaData
# from sqlalchemy import Table,Column,Integer,String


# engine = create_engine('sqlite://///home/martogod/Python_Formal/week_12/my_database.db',echo=True)

# metadata=MetaData()

# user=Table('users',metadata,
#         Column('id', Integer, primary_key=True),
#         Column('name', String),
#         Column('fullname', String),
# )

# metadata.create_all(engine)


# query_to_be_exe=user.insert().values(id=1,name="Nesho",fullname="Neshto po-dulgo")

# c=engine.connect()
# c.execute(query_to_be_exe)