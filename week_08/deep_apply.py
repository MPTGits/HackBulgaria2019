#Updating given values by a key

primitive=[bool,int,str,float]

def deep_apply_DFS(data, key,new_value):
    if type(data) in primitive:
        return
    for k, v in data.items():
        if k==key:
            data[k]=new_value
        elif type(v)==list:
            for i in v:
                value=deep_apply_DFS(i, key,new_value) 
        elif type(v) == dict:
            value = deep_apply_DFS(v, key,new_value)


# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female','addon':
#                                                                     {'test':[{'test_key':23,
#                                                                             '  something':12},
#                                                                             {'good_stuff':11},
#                                                                             12]}},
#         'test':"nOt A tEsT"}


# deep_apply_BFS(people,'test',39)
# print(people)