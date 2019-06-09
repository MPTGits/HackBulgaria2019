from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
from utils.constant_variables import DatabaseConstants


#Creating an engine so that we can communicate with the database
#Note that, creating an engine does not connect to the database instantly. This process is postponed to when it's needed
engine = create_engine('sqlite:////home/martogod/Python_Formal/week_11/database/'+DatabaseConstants.MAIN_DATABASE_NAME)
    #home/martogod/101_Python_Formal/week_11/database/main_database.db')  
#his means that all modifications tracked by Sessions (Units of Works) will be applied to the underlying database together, or none of them will.
# In other words, Sessions are used to guarantee the database consistency.
Session = sessionmaker(bind=engine)

#Base class from which we want to derive
Base = declarative_base()

session = Session();

