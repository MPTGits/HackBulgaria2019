def sum_of_digits(n):
    num=str(n)
    final_sum=0
    for digit in num:
        final_sum+=int(digit)
    return final_sum

# print(sum_of_digits(432)==9)
# print(sum_of_digits(4432)==13)
# print(sum_of_digits(132)==6)

def to_digits(n):
    result_list=list(str(n))
    return list(map(int,result_list))

# print(to_digits(123)==[1,2,3])
# print(to_digits(99999)==[9,9,9,9,9])
# print(to_digits(33410)==[3,3,4,1,0])

def to_number(digits):
    str_list_of_digits=list(map(str,digits))
    return int(''.join(str_list_of_digits))

# print(to_number([1,2,3])==123)
# print(to_number([9,9,9,9,9])==99999)
# print(to_number([1,2,3,0,2,3])==123023)
# print(to_number([21,2,33])==21233)

def fact(n):
    n=int(n)
    if n==0:
        return 1 
    return n*fact_digits(n-1)

from functools import reduce

def fact_digits(n):
    fact_list=list(map(fact,list(str(n))))
    return reduce(lambda x,y:x+y,fact_list)

# print(fact_digits(111)==3)
# print(fact_digits(145)==145)
#print(fact_digits(999)==1088640)

def palindrome(n):
    n=str(n)
    return n==n[::-1]

# print(palindrome(121)==True)
# print(palindrome('baba')==False)
# print(palindrome('kapak')==True)

def count_vowels(str):
    dic_vowels='aeiouy'
    vowels_found=0
    for letter in str:
        if letter.lower() in dic_vowels:
            vowels_found+=1
    return vowels_found

# print(count_vowels("Python")==2)
# print(count_vowels("Theistareykjarbunga")==8)
# print(count_vowels("grrrrgh!")==0)
# print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!")==22)

def count_consonants(str):
    dic_consonants='bcdfghjklmnpqrstvwxz'
    consonants_found=0
    for letter in str:
        if letter.lower() in dic_consonants:
            consonants_found+=1
    return consonants_found

# print(count_consonants("Python")==4)
# print(count_consonants("Theistareykjarbunga")==11)
# print(count_consonants("grrrrgh!")==7)
# print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!")==44)

#Credits to Alex :D
def char_histogram(string):
    result_dict = dict.fromkeys(string, 0)
    for letter in string:
        result_dict[letter] += 1
    return result_dict

# print(char_histogram("Python!")=={ 'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1 })
# print(char_histogram("AAAAaaa!!!")=={ 'A': 4, 'a': 3, '!': 3 })

def sum_matrix(m):
    result_sum=0
    for row in m:
        result_sum+=reduce(lambda x,y:x+y,row)
    return result_sum

# print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])==45)
# print(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])==0)
# print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])==55)

def nan_expand(times):
    if times==0:
        return ''
    return 'Not a '*times + 'NaN'

# print(nan_expand(0)=='')
# print(nan_expand(1)=="Not a NaN")
# print(nan_expand(2)=='Not a Not a NaN')
# print(nan_expand(3)=="Not a Not a Not a NaN")

# def get_nearest_prime(old_number):
#     largest_prime = 0
#     for num in range(old_number + 1, 2 * old_number) :
#         for i in range(2,num):
#             if num % i == 0:
#                 break
#         else:
#             largest_prime = num
#     return largest_prime



# def prime_factorization(n):
#     result_list=[]
#     prime_num=2
#     divadiable=0
#     current_result=[]
#     while :
#         if n%prime_num==0:
#             while n%prime_num==0:
#                 divadiable+=1
#                 n=n/prime_num
#                 current_result.append(prime_num)
#           s  result_list.append((prime_num,divadiable))
#             divadiable=0
#         else:
#             prime_num=get_nearest_prime(prime_num)

def group(lst):
    current_list=[]
    result_list=[]
    while len(lst)>1:
        for x in range(len(lst)-1):
            if lst[x]==lst[x+1]:
                current_list.append(lst[x])
                continue
            current_list.append(lst[x])
            break
        lst=lst[len(current_list):]
        if len(lst)==1:
            current_list=current_list+[current_list[0]]
        result_list.append(current_list)
        current_list=[]

    return result_list

# print(group([1, 1, 1, 2, 3, 1, 1])==[[1, 1, 1], [2], [3], [1, 1]])
# print(group([1, 2, 1, 2, 3, 3])==[[1], [2], [1], [2], [3, 3]])

def max_consecutive(items):
    consec_lists=group(items)
    return len(max(consec_lists,key=lambda x:len(x)))

# print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3])==4)
# print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5])==3)

