#First implementation(lost) changed the tank size and compared with it 
#this once realies on changing passed and current stations
def gas_stations(distance, tank_size, stations):
    stations.append(distance)
    fewest_visited_stations = []
    last_passed = stations[0]
    last_stat_stoped = 0
    for station in stations[1:]:
        if station - last_stat_stoped > tank_size:
            fewest_visited_stations.append(last_passed)
            last_stat_stoped = last_passed
        elif last_stat_stoped - station == tank_size:
            fewest_visited_stations.append(station)
            last_stop = station
        last_passed = station
    return fewest_visited_stations

#print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))

from functools import reduce

def is_number_balanced(number):
    number=str(number)
    if len(number)==1:
        return True 
    list_digits=list(map(int,list(number)))
    if len(number)%2==0:
        return reduce(lambda x,y:x+y,list_digits[:(len(list_digits)//2):])==reduce(lambda x,y:x+y,list_digits[len(list_digits)//2::])
    return reduce(lambda x,y:x+y,list_digits[:(len(list_digits)//2):])==reduce(lambda x,y:x+y,list_digits[len(list_digits)//2+1::])

# print(is_number_balanced(4518))
# print(is_number_balanced(1238033))
# print(is_number_balanced(9))
# print(is_number_balanced(28471))

def increasing_or_decreasing(seq):
    lst_up=[seq[x] for x in range(len(seq)-1) if seq[x]<seq[x+1]]+seq[len(seq)-1::]
    lst_down=[seq[x] for x in range(len(seq)-1) if seq[x]>seq[x+1]]+seq[len(seq)-1::]
    if len(lst_up)==len(seq):
        return 'UP!'
    elif len(lst_down)==len(seq):
        return 'Down!'
    return False 

# print(increasing_or_decreasing([1,2,3,4,5])=='UP!')
# print(increasing_or_decreasing([5,6,-10])==False)
# print(increasing_or_decreasing([1,1,1,1])==False)
# print(increasing_or_decreasing([9,8,7,6])=='Down!')

def get_largest_palindrome(n):
    n=str(n-1)
    while n!=n[::-1]:
        n=str(int(n)-1)
    return int(n)

# print(get_largest_palindrome(99)==88)
# print(get_largest_palindrome(252)==242)
# print(get_largest_palindrome(994687)==994499)
# print(get_largest_palindrome(754649)==754457)

import re 

def sum_of_numbers(input_string):
    list_numbers=re.findall('\d+',input_string)
    if list_numbers==[]:
        list_numbers.append(0)
    list_numbers=map(int,list_numbers)
    return reduce(lambda x,y:int(x)+int(y),list_numbers)

# print(sum_of_numbers("ab125cd3"))
# print(sum_of_numbers("ab12"))
# print(sum_of_numbers("ab"))
# print(sum_of_numbers("1101"))
# print(sum_of_numbers("1111O"))
# print(sum_of_numbers("1abc33xyz22"))
# print(sum_of_numbers("0hfabnek"))

def birthday_ranges(birthdays, ranges):
    peopleBronInRanges=[]
    for index in range(len(ranges)):
        peopleBronInRanges.append(len(list(filter(lambda x:x>=ranges[index][0] and x<=ranges[index][1],birthdays))))
    return peopleBronInRanges

# print(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)])==[2, 3, 4, 5, 2])
# print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)])==[5, 2, 0, 1])


#Creats tuple of kind (digit,consecetive repetitions)
def creat_tuples(lst):
    result_list=[]
    repetitions=1
    for index in range(len(lst)-1):
        if lst[index]==lst[index+1]:
            repetitions+=1
            continue
        result_list.append((lst[index],repetitions))
        repetitions=1
        if index==len(lst)-2 and repetitions==1:
             result_list.append((lst[index+1],repetitions))
    
    if repetitions>1:
        result_list.append((lst[len(lst)-1],repetitions))

    return result_list

# print(creat_tuples([2, -1, 2, 2, -1, 2, 2, 1]))
# print(creat_tuples([2, 2, 2, 2]))
# print(creat_tuples([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))



def numbers_to_message(pressed_sequence):
    dic_char_to_numbers={
    0:' ',
    2:'abc',
    3:'def',
    4:'ghi',
    5:'jkl',
    6:'mno',
    7:'pqrs',
    8:'tuv',
    9:'wxyz'
    }
    tuples_list=creat_tuples(pressed_sequence)
    result_list=[]
    next_one_capital=False
    for (value,repetitions) in tuples_list:
        if value==-1:
            continue
        if value==1:
            next_one_capital=True
            continue
        if next_one_capital==True:
            result_list.append(dic_char_to_numbers[value][(repetitions-1)%len(dic_char_to_numbers[value])].upper())
            next_one_capital=False
            continue
        result_list.append(dic_char_to_numbers[value][(repetitions-1)%len(dic_char_to_numbers[value])])
    return ''.join(result_list)

# print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))
# print(numbers_to_message([2, 2, 2, 2]))
# print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))


def elevator_trips(people_weight, people_floors, elevator_floors, max_people, max_weight):
    if len(people_weight)!=len(people_floors) or (people_weight==[] and people_floors==[]):
        raise ValueError("Sorry unmatching number of people and floors to go!")
    current_people=0
    current_weight=0
    end_point=0
    trips=0
    while people_floors!=[]:
        while current_weight+people_weight[end_point]<max_weight and current_people<max_people and  end_point<len(people_weight)-1:
            current_weight+=people_weight[end_point]
            current_people+=1
            end_point+=1
        trips+=len(set(people_floors[:end_point:]))+1
        current_people=0
        current_weight=0
        people_floors=people_floors[end_point::]
        

    return trips


# print(elevator_trips([40, 40, 100, 80, 60], [2, 3, 3, 2, 3], 3, 5, 200))
# print(elevator_trips([80, 60, 40], [2, 3, 5], 5, 2, 200))