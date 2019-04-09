import sys
from random import randint


def generate_numbers(filename, numbers):
    with open(filename,'w+') as f:
        for num in range(int(numbers)):
            f.write(str(randint(1,10000))+' ')


def main():
    filename=sys.argv[1]
    numbers=sys.argv[2]
    generate_numbers(filename,numbers)

if __name__ == '__main__':
    main()