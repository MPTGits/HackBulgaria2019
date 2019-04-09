def parse_changes_to_file(file_name,user_data):
    f=open(file_name,'w')
    for k,v in user_data.items():
        f.write('===='+k+'===='+'\n')
        for subKey,subValue in v.items():
            for items in subValue:
                f.write(str(items[0])+','+items[1]+','+subKey+'\n')
    f.close()

def list_user_data(all_user_data):
    return all_user_data

def show_user_income(all_user_data):
    result_list=[]
    for k,v in all_user_data.items():
        for subKey,subValue in v.items():
            if(subKey=='income'):
                result_list+=subValue
    return result_list

def show_user_savings(all_user_data):
    result_list=[]
    for k,v in all_user_data.items():
        for subKey,subValue in v.items():
            if(subKey=='income'):
                    result_list+=[items for items in subValue if 'Savings' in items]
    return result_list

def show_user_deposits(all_user_data):
    result_list=[]
    for k,v in all_user_data.items():
        for subKey,subValue in v.items():
            if(subKey=='income'):
                    result_list+=[items for items in subValue if 'Deposit' in items]
    return result_list

def show_user_expenses(all_user_data):
    result_list=[]
    for k,v in all_user_data.items():
        for subKey,subValue in v.items():
            if(subKey=='expense'):
                result_list+=subValue
    return result_list

def list_user_expenses_ordered_by_categories(all_user_data):
    expenses_list=show_user_expenses(all_user_data)
    expenses_list.sort(key=lambda tuple: tuple[1])
    return expenses_list

def show_user_data_per_date(date, all_user_data):
    result_list=[]
    for k,v in all_user_data.items():
        if k==date:
            for subKey,subValue in v.items():
                result_list+=[(int(value[0]),value[1],'New '+subKey.title()) for value in subValue]
            break
    result_list.sort(key=lambda tuple: tuple[1])
    return result_list

def add_income(income_category, money, date, all_user_data,filename):
    for k,v in all_user_data.items():
        if k==date:
            for subKey in v:
                if subKey=='income':
                    v[subKey].append((money,income_category))
                    break
    parse_changes_to_file(filename,all_user_data)

def add_expense(expense_category, money, date, all_user_data,filename):
    for k,v in all_user_data.items():
        if k==date:
            for subKey in v:
                if subKey=='expense':
                    v[subKey].append((money,expense_category))
                    break
    parse_changes_to_file(filename,all_user_data)

all_user={'Martin':{'22-03-2019': {'income': [(10, 'Deposit'),(20,'Savings')], 'expense': [(27.7, 'Food')]}, '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}}

def main():
    user=input('Your name is:')
    while user not in all_user:
        print('Non existing name!')
        user=input('Your name is:')
    parse_changes_to_file('money_tracker.txt',all_user[user])
    while True:
        with open('money_tracker.txt','r') as f:
            option=input("Welcome to the money tracker "+user+" pick and option:"+'\n'+'1)Show all data'+'\n'+'2)Show expenses'+'\n'+'3)Show data per date'+'\n'+'4)Add new expense'+'\n'+'5)Add new income'+'\n'+'6)Show user deposits'+'\n'+'7)Exit'+'\n')   
            if int(option)<=0 and int(option)>=7:
                continue
            
            elif option=='1':
                print(f.read())
            
            elif option=='2':
                for line in f:
                    if 'expense' in line:
                        print(line)
            
            elif option=='3':
                date=input('Input a date to view data from:')
                found=False
                for line in f:
                    if found and '=' not in line:
                        print(line)
                        continue
                    if date in line:
                        print(line)
                        found=True
                        continue
                    if found:
                        break

            elif option=='4':
                category=input('New expense category:')
                value=input('Expense value:')
                date=input('Input date of expnse:')
                add_expense(category,value,date,all_user[user],'money_tracker.txt')
            
            elif option=='5':
                category=input('New income category:')
                value=input('Income value:')
                date=input('Input date of income:')
                add_income(category,value,date,all_user[user],'money_tracker.txt')
            
            elif option=='6':
                for line in f:
                    if 'deposit' in line or 'Deposit' in line:
                        print(line)
            
            elif option=='7':
                break

if __name__=='__main__':
    main()

#show_user_income(c
#print(show_user_savings({'22-03-2019': {'income': [(10, 'Deposit'),(20,'Savings')], 'expense': [(27.7, 'Food')]}, '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}))
#print(list_user_expenses_ordered_by_categories({'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'F'),(40.2,'A')]}, '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'E'),(2,'B')]}}))
#print(show_user_data_per_date('23-03-2019', {'22-03-2019': {'expense': [(5.5, ' Eating Out'), (34.0, ' Clothes'), (41.79, ' Food'), (12.0, ' Eating Out'), (7.0, ' House'), (14.0, ' Pets'), (112.4, ' Bills'), (21.5, ' Transport')], 'income': [(760.0, ' Salary')]}, '23-03-2019': {'expense': [(15.0, ' Food'), (5.0, ' Sports')], 'income': [(50.0, ' Savings'), (200.0, ' Deposit'), (10.0, ' Deposit')]}}))
#add_income('Smth',69,'23-03-2019',{'22-03-2019': {'expense': [(5.5, ' Eating Out'), (34.0, ' Clothes'), (41.79, ' Food'), (12.0, ' Eating Out'), (7.0, ' House'), (14.0, ' Pets'), (112.4, ' Bills'), (21.5, ' Transport')], 'income': [(760.0, ' Salary')]}, '23-03-2019': {'expense': [(15.0, ' Food'), (5.0, ' Sports')], 'income': [(50.0, ' Savings'), (200.0, ' Deposit'), (10.0, ' Deposit')]}})
#add_expense('Smth',69,'23-03-2019',{'22-03-2019': {'expense': [(5.5, ' Eating Out'), (34.0, ' Clothes'), (41.79, ' Food'), (12.0, ' Eating Out'), (7.0, ' House'), (14.0, ' Pets'), (112.4, ' Bills'), (21.5, ' Transport')], 'income': [(760.0, ' Salary')]}, '23-03-2019': {'expense': [(15.0, ' Food'), (5.0, ' Sports')], 'income': [(50.0, ' Savings'), (200.0, ' Deposit'), (10.0, ' Deposit')]}})