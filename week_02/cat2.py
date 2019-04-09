# cat2.py
import sys 

def cat2(arguments):
    for file in  arguments:
        with open(file,'r') as f:
            print(f.read())



def main():
    fileNames=sys.argv[1:]
    cat2(fileNames)

if __name__ == '__main__':
    main()