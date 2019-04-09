class Bill:
    def __init__(self,amount):
        self.amount=amount

    def __str__(self):
        return 'A '+str(self.amount)+'$ bill!'

    def __repr__(self):
        return self.__str__

    def __eq__(self,other):
        return self.amount==other.amount

    def __hash__(self):
        return hash(self.amount)

    def __int__(self):
        return int(self.amount)

# a = Bill(10)
# b = Bill(5)
# c = Bill(10)

# print(int(a)) # 10
# print(str(a)) # "A 10$ bill"
# print(a) # A 10$ bill

# print(a == b) # False
# print(a == c) # True)

class  BillBatch:

    def __init__(self,bills):
        self.bills=bills
        self.idx=0

    def __len__(self):
        return len(self.bills)

    def total(self):
        return sum([x for x in self.bills])

    def __iter__(self):
       return self
   
    def __repr__(self):
        return self.bills

    def __next__(self):
        self.idx += 1
        try:
            return self.bills[self.idx-1]
        except IndexError:
            self.idx = 0
            raise StopIteration  

# values = [10, 20, 50, 100]
# bills = [Bill(value) for value in values]

# batch = BillBatch(bills)

# for bill in batch:
#     print(bill)
from functools import reduce

class CashDesk:

    def __init__(self):
        self.current_money=0
        self.bills_sorted={}

    def take_money(self,money):
        if isinstance(money,Bill):
            self.current_money+=int(money)
            self.bills_sorted[str(int(money))+'$ bills:']=self.bills_sorted.get(int(money),0)+1
        elif isinstance(money,BillBatch):
            self.current_money+=reduce(lambda x,y:int(x)+int(y),money)
            for x in money:
                self.bills_sorted[str(int(x))+'$ bills:']=self.bills_sorted.get(int(x),0)+1

    def total(self):
        return 'Current total money:'+str(self.current_money)

    def inspect(self):
        return self.bills_sorted


# values = [10, 20, 50, 100, 100, 100]
# bills = [Bill(value) for value in values]

# batch = BillBatch(bills)

# desk = CashDesk()

# desk.take_money(batch)
# desk.take_money(Bill(10))

# print(desk.total()) # 390
# print(desk.inspect())
