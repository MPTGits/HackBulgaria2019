primitive=[bool,int,str,float]

def deep_find_DFS(data, key):
    if data in primitive:
        return
    for k, v in data.items():
        if k==key:
            return v
        elif type(v)==list:
            for i in v:
                value=deep_find_DFS(i, key) 
                if value:
                    return value
        elif type(v) == dict:
            value = deep_find_DFS(v, key)
            if value:
                return value


def deep_find_BFS(data, key):
    queue=[]
    for k,v in data.items():
        queue.append((k,v))
    while queue!=[]:
        element=queue.pop(0)
        if key==element[0]:
            return element[1]
        elif type(element[1])==list:
            for values in element[1]:
                if type(values)==dict:
                    for k,v in values.items():
                        queue.append((k,v))
        elif type(element[1])==dict:
            for k,v in element[1].items():
                queue.append((k,v))




# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female','addon':
#                                                                     {'test':[{'test_key':23,
#                                                                             '  something':12},
#                                                                             {'good_stuff':11},
#                                                                             12]}}}


# print(deep_find_BFS(people,'test_key'))