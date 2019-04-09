import sys

def reduce_file_path(path):
    lst_path=path.split('/')
    lst_path=list(filter(lambda x:'/' not in x,lst_path))
    lst_path=list(filter(lambda x:x is not ''  ,lst_path))
    reduced_path='/'
    last_dir=''
    for file in lst_path:
        if file =='..':
            reduced_path=reduced_path[:-len(last_dir)-1]
            continue
        elif file is '.':
            continue
        reduced_path=reduced_path+ file +'/'
        last_dir=file
    if len(reduced_path)<=1:
        return '/'
    return ''.join(reduced_path)[:-1]


print(reduce_file_path('/'))
print(reduce_file_path("/srv/../"))
print(reduce_file_path("/srv/www/htdocs/wtf/"))
print(reduce_file_path("/srv/www/htdocs/wtf"))
print(reduce_file_path("/srv/./././././"))
print(reduce_file_path("/srv/./././././"))
print(reduce_file_path("/etc//wtf/"))
print(reduce_file_path("/../"))
print(reduce_file_path("/etc/../etc/../etc/../"))

# def main():
#     path=sys.argv[1]
#     reduce_file_path(path)

# if __name__=='__main__':
#     main()