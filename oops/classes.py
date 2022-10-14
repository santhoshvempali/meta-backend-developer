class myclass:
    a=10
    def data(self):
        return "hi"
myc=myclass()
print(myc.a)
print(myc.data())


class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2

    def cost_evaluation(self, rate):
        # Functionality to calculate the costs from the area of the house
        cost = rate * self.num_rooms
        return cost



house = House()
print(house.num_rooms)
print(House.num_rooms)
house.num_rooms = 7
# House.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)


value = 7
class A:
    value = 5
a = A()
a.value = 3
print(value)

class Recepie:
    def __init__(self,dish,items,time) -> None:
        self.dish=dish
        self.items=items
        self.time=time
    def contents(self):
        print("the dish is"+ self.dish+"the items used are"+str(self.items))

pizza=Recepie("pizza",["dough","veggies","sauce"],45)
print(pizza.dish)
print(pizza.contents())



class MyFirstClass():
    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book)

whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")