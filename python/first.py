"""name = input("name: ")
print(f"hello, {name}")
n = int(input("number: "))

 if n > 0:
     print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")
name = ["harry", "robin", "luffy"] # lsit
print(name[0])

name = (10.0, 20.0) # tuple
print(name)

# define a list of names
names = ["robin", "name", "sanji", "ginny"] 

#print(names[0])

names.append("draco")

names.sort() # sorts the list alphabitacally
print(names)

#creat an empty set
s = set() 

#add elements ti set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(1) # wont add it to the set. as every element appears only once in a set

s.remove(2)
print(s)

print(f"the set has {len(s)} elements.")


#loops
#for i in [0, 1, 2, 3, 4, 5]:
for i in range(6):
    print(i)

# loops 
names = ["robin", "name", "sanji", "ginny"]
for name in names:
    print(name)

# loops

name = "harry"

for character in name:
    print(character)
    
# loops with dictionary
houses = {"Harry": "gryffindor", "draco": "slynderin"}

houses["harmione"] = "gryffindor"

print(houses["harmione"])



# functions

def square(x):
    return x*x


for i in range(10):
    print(f"The square of {i} is {square(i)}")

# to use function square in other files 
# we can add>>> from (name of the file we will be importing square function) import square
# or
# >>>import functions   and whereever we want to use the function we have to mention the name of the file we are importing the function from e.g : funtions.square()"""
"""

# classess

class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2


p = Point(2, 8)
print(p.x)
print(p.y)"""


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []


    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["harry", "ron", "hermanione", "ginny"]
for person in people:
    
    if flight.add_passenger(person):
        print(f"added {person} to flight successfully.")
    else:
        print(f"no available seats for {person}")











