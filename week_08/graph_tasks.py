
def DFS_visit(data,k,key,checked_elemetnts):
    checked_elemetnts.append(k)
    if k==key:
        return print(data[k])
    
    if type(data[k]) is dict:
        for next_k,v in data[k].items():
            if next_k not in  checked_elemetnts:
               DFS_visit(data[k],next_k,key,checked_elemetnts)
    
    #Checking for a list seperatly?
    if type(data[k]) is list:
        for element in data[k]:
            if type(element) is dict:
                for next_k,v in element.items():
                    if next_k not in  checked_elemetnts:
                       DFS_visit(element,next_k,key,checked_elemetnts)


def deep_find_DFS(data, key):
    checked_elemetnts=[]
    for k,v in data.items():
        DFS_visit(data,k,key,checked_elemetnts)



# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female','addon':
#                                                                     {'test':[{'test_key':23,
#                                                                             '  something':12},
#                                                                             {'good_stuff':11},
#                                                                             12]}}}


# print(deep_find_DFS(people,'test_key'))