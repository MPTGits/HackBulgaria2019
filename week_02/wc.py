import sys
from random import randint


def wc(command, filename):
    with open(filename,'r') as f:
        if command=='chars':
            return len([char for char in f.read()])
        elif command=='words':
            return len(f.read().split())
        elif command=='lines':
            return sum(1 for line in f)

def main():
    command=sys.argv[1]
    filename=sys.argv[2]
    print(wc(str(command),filename))

if __name__ == '__main__':
    main()