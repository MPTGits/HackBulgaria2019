import csv


def my_filter(file_name,**kwargs):
    lst = []
    with open(file_name, 'r') as f_input:
        csv_input=csv.DictReader(f_input)
        for person in csv_input:
            if all(v in person[k] for k, v in kwargs.items()):
                lst.append(person)
    return lst

print(my_filter('example_data.csv',full_name="Karen")

def my_filter_counts(file_name,**kwargs):
    lst = list()
    with open(file_name, 'r') as f_input:
        csv_input=csv.DictReader(f_input)
        for line in csv_input:
            if all(v in line[k] for k, v in kwargs.items()):
                lst.append(line)
    return len(lst)

print(my_filter_counts('example_data.csv',full_name="Karen"))