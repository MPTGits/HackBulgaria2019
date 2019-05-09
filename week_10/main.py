from BusinessCardCatalog import creat_user_table,add,delete,get,list_users,help_opt

def main():
    database_name=input("Enter the name of your database:")
    creat_user_table(database_name)
    user_input=''
    while user_input!='exit':
        user_input=input("""Welcome to the business card catalog please select and option\n
            Enter a command(or type help for information of the commands):
            """)
        if user_input=='add':
            add(database_name)
        elif user_input=='list':
            print(list_users(database_name))
        elif user_input=='get':
            print(get(database_name))
        elif user_input=='delete':
            delete(database_name)
        elif user_input=='help':
            help_opt()

if __name__=='__main__':
    main()
