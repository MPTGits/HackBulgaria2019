import sys
from functools import reduce
#sum numbers

def sum_numbers(filename):
    with open(filename,'r') as f:
        numbers=f.read()
        lst_numbers=numbers.split(' ')
    return reduce(lambda x,y:int(x)+int(y),lst_numbers[:len(lst_numbers)-1:])


def main():
    filename=sys.argv[1]
    print(sum_numbers(filename))

if __name__ == '__main__':
    main()