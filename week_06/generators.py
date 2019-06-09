def chain(iterable_one, iterable_two):
    res=[]
    for el in iterable_one:
        res.append(el)
        #yield el
    for el in iterable_two:
        res.append(el)
        #yield el
    return iter(res)

#res=chain(range(0,4),range(2,8))

def compress(iterable, mask):
    result_list=[]
    lst=iter(iterable)
    for el in mask:
        if el:
            curr_el=next(lst)
            yield curr_el
            result_list.append(curr_el)
            continue
        curr_el=next(lst)
    return result_list

# res=compress(["Ivo", "Rado", "Panda"], [False, False, True])
# print(res)
# print(list(res))

def cycle(iterable):
        while True:
            yield iter(iterable)

# endless = cycle(range(0,10))
# for item in endless:
#     print(item)

#Book Reader

def BookReader(fileName):
    current_chapter=''
    book=open(fileName,'r')
    lines=book.readlines()
    for line in lines:
        part_of_book=open(line[:len(line)-1:],'r')
        lines_part_of_book=part_of_book.readlines()
        for line_of_part_book in lines_part_of_book:
            if line_of_part_book[0]=='#':
                yield current_chapter
                current_chapter=''
            current_chapter+=line_of_part_book
    return False

def going_throught_chapters(fileName):
    chapter_by_chapter=BookReader(fileName)
    while chapter_by_chapter!=False:
        pressed_key=input('Press spacebar')
        if pressed_key!=' ':
            continue
        print(next(chapter_by_chapter))

# going_throught_chapters('book.txt')

import random

#Book Generator
def book_generator(num_chapters,chapter_length):
    dic_file=open('/etc/dictonaries-common/words','r')
    chapter='1'
    while chapter<num_chapters:
        max_words=random.randint(0, chapter_length)
        curr_words=0
        chapter_file=open(chapter+'.txt','w+')
        while curr_words<max_words:
            ran_word=random.randint(0,len(dic_file))
            

import os
import pyautogui


#needs [sudo apt install sox]
def current_mouse_poss():
    while True:
        x,y=pyautogui.position()
        if x<600 and y<500:
            os.system("say 'Sansa Stark dies in Game of Thrones' &")
        yield (x,y)

# gen=current_mouse_poss()
# while True:
#     print(next(gen))