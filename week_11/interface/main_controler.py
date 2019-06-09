import re
import sys
import uuid
import hashlib
import sys
from hospital.main_database import *
from utils.exceptions import *
from utils.constant_variables import DatabaseConstants
from hospital.user import User

# #Creating an engine so that we can communicate with the database
# #Note that, creating an engine does not connect to the database instantly. This process is postponed to when it's needed
# engine = create_engine('sqlite:////home/martogod/Python_Formal/week_11/database/'+DatabaseConstants.MAIN_DATABASE_NAME)
#     #home/martogod/101_Python_Formal/week_11/database/main_database.db')  
# #his means that all modifications tracked by Sessions (Units of Works) will be applied to the underlying database together, or none of them will.
# # In other words, Sessions are used to guarantee the database consistency.
# Session = sessionmaker(bind=engine)

# session = Session();

class SigningControler:

    @classmethod
    def login(cls,username,password):
        users=session.query(User).all()
        for user in users:
            if username==user.username and cls.__hash_with_salt(password,user.hashed_password.split(":")[1])==user.hashed_password.split(":")[0]:
                return user
        raise InvalidUserData

    @classmethod
    def register(cls,username,password,confirmation_password,status=None):
        cls.__validate_password(password)

        users=session.query(User).all()
        for user in users:
            if username==User.username and __hash_with_salt(password,User.password.split(":")[1])==User.password:
                raise ExistingUser
        
        hashed_pass=cls.__hash_password(password)
        confirmation_hashed_pass=cls.__hash_with_salt(confirmation_password,hashed_pass.split(":")[1])
        

        if hashed_pass.split(":")[0]!=confirmation_hashed_pass:
            raise UnmatchingPasswords

        if not username.isalpha():
            raise InvalidUsername

        user=User(username,hashed_pass,status)

        session.add(user)
        session.commit()

        return user

    def __hash_with_salt(password,salt):
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest()

    def __hash_password(password):
        salt = uuid.uuid4().hex
        return (hashlib.sha256(salt.encode() + password.encode()).hexdigest()+":"+salt)

    @staticmethod
    def __validate_password(password):
        if len(password) < 8:
            print("Make sure your password is at lest 8 letters")
            sys.exit(1)
        elif re.search('[0-9]',password) is None:
            print("Make sure your password has a number in it")
            sys.exit(1)
        elif re.search('[A-Z]',password) is None: 
            print("Make sure your password has a capital letter in it")
            sys.exit(1)


