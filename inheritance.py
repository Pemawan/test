class person:
    def __init__(self, name, age, CID_number):
        self.name = name
        self.age = age
        self.CID_number = CID_number
    
    def behavior (self, walk, talk, eat, sleep):
        self.walk = walk
        self.talk = talk
        self.eat = eat
        self.sleep = sleep

Nm = input ("write the name of a person :")
A = input ("what is thee age of the person: ")
ID = input ("what is the persons CID_ number: ")
print ("\n")

p1 = person(Nm, A, ID)
p1.behavior("walking", "talking", "eating", "sleeping")

print(f"Name: {p1.name}, Age: {p1.age}, CID Number: {p1.CID_number}")
print(f"Behavior: Walk - {p1.walk}, Talk - {p1.talk}, Eat - {p1.eat}, Sleep - {p1.sleep}")
print ("\n")