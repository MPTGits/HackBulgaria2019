# cat.py
import sys

def cat(argument):
    with open(argument,'r') as f:
        print(f.read())


def main():
    filename=sys.argv[1]
    cat(filename)

if __name__ == '__main__':
    main()