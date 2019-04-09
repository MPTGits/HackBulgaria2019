#duhs implementation

import sys
import os 

def du_hs(paths):
    files_in_directory = []
    for (dirpath, dirnames, filenames) in os.walk(paths):
        for file in filenames:
                files_in_directory.append(os.path.join(dirpath, file))


    files_size=0
    for files in files_in_directory:
        files_size+=int(os.path.getsize(files))

    print(round((float(files_size/1000000000)),5),end='')
    print("GB")



def main():
    du_hs(sys.argv[1])

if __name__ == '__main__':
    main()