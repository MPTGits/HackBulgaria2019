def accepts(*types):
    def func_impl(func):
        def type_checker(*values):
            for index in range(len(types)):
                if types[index]!=type(values[index]):
                    raise TypeError ('Argument ' +str(index)+' is not of type '+str(types[index]))
            return func(*values)
        return type_checker
    return func_impl
        

def encrypt(shifter):
    def func_impl(func):
        def shifting():
            result=func().split(' ')
            new_name=[]
            shifted_word=[]
            for word in result:
                shifted_word=[chr(ord(letter) + shifter) for letter in word]
                new_name.append(''.join(shifted_word))
                shifted_word=[]
            return ' '.join(new_name)
        return shifting
    return func_impl

import datetime

def log(filename):
    def func_impl(func):
        def log_date_started(*args):
            with open(filename, 'a') as f:
                f.write(str(func.__name__)+' was called at '+str(datetime.datetime.now())+'\n')
                return func(*args)
        return log_date_started
    return func_impl

import time

def performance(filename):
    def func_impl(func):
        def log_execution_time(*args):
            start = time.time()
            with open(filename, 'a') as f:
                f.write(str(func.__name__)+'was called and took '+ str(time.time() - start)[:3:]+' seconds to complete'+'\n')
                return func(*args)
        return log_execution_time
    return func_impl


#Test for accept

# @accepts(str, int)
# def deposit(name, money):
#     print("{} sends {} $!".format(name, money))
#     return True

# @accepts(str)
# def say_hello(name):
#     return "Hello, I am {}".format(name)

#Test for encrypt

# @encrypt(2)
# def get_low():
#     return "Get get get low"

# print(get_low())

#Test for log

# @log('log.txt')
# @encrypt(2)
# def get_low():
#     return "Get get get low"

# print(get_low())

#Test for performance

# @performance('log.txt')
# def something_heavy():
#     time.sleep(2)
#     return "I am done!"

# something_heavy()