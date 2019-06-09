#Finding all the values with the given key and not only the first one
primitive=[bool,int,str,float]

def deep_find_DFS_all(data, key,values=[]):
    if type(data) in primitive:
        return
    for k, v in data.items():
        if k==key:
            values.append(v)
        elif type(v)==list:
            for i in v:
                value=deep_find_DFS_all(i, key,values) 
        elif type(v) == dict:
            value = deep_find_DFS_all(v, key,values)


def deep_find_BFS_all(data, key,final_values=[]):
    queue=[]
    for k,v in data.items():
        queue.append((k,v))
    while queue!=[]:
        element=queue.pop(0)
        if key==element[0]:
            final_values.append(element[1])
        elif type(element[1])==list:
            for values in element[1]:
                if type(values)==dict:
                    for k,v in values.items():
                        queue.append((k,v))
        elif type(element[1])==dict:
            for k,v in element[1].items():
                queue.append((k,v))