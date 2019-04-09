#Are two words anagrams?

def anagrams():
    print('Input the first word:')
    word1=input()
    print('Input the second word:')
    word2=input()
    if sorted(word1)==sorted(word2):
        return 'ANAGRAMS'
    return 'NOT ANAGRAMS'

#print(anagrams())

from functools import reduce

def is_credit_card_valid(number):
    number=[int(x) for x in str(number)]
    if len(number)%2==0:
        return False
    for index in range(len(number)):
        if index%2!=0:
            number[index]=number[index]*2
    number=''.join(map(str,number))
    number=[int(x) for x in number]
    if reduce(lambda x,y:x+y,number)%10==0:
        return True
    return False

# print(is_credit_card_valid(79927398713))
# print(is_credit_card_valid(79927398713))
# print(is_credit_card_valid(79927398715))

def list_of_primes(n):
    primes = []
    for y in range (2, n):
        for z in range(2, y):
            if y % z == 0:
                break
        else:
            primes.append(y)
    primes.sort()
    return primes

def goldbach(n):
    prime_tuples=[]
    for x in list_of_primes(n):
        for y in list_of_primes(n):
            if (y,x) not in prime_tuples:
                prime_tuples.append((x,y))
    result_list=[x for x in prime_tuples if x[0]+x[1]==n]
    return result_list

# print(goldbach(100))
# print(goldbach(10))
# print(goldbach(8))
# print(goldbach(6))
# print(goldbach(4))