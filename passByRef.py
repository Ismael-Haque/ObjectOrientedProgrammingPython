class Car:
    def __init__(self, name):
        self.name = name
        print(id(self))

ford = Car("Ford")
print(ford.name)


def feature(car, new_name):
    print("Name : ", car.name)
    print(id(car))
    car.name = new_name

feature(ford, "Audi")

print(id(ford))

print(ford.name)

# Main takeaway from this set of code is the changes we make to a object through other functions or any other ways also changes the object's property/attribute as they have same reference id (or place in memory)

# this is called mutatble object
# list and dictionary is mutable
# tuple is immutable