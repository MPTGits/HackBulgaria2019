class Zoo:
    def __init__(self):
        self.animals=[]

    def add_animal(self,animal_name):
        self.animals.append(animal_name)

    def __iter__(self):
        return self

    def __next__(self):
        index=self.index
        self.index+=1
        return self.animals[index]
