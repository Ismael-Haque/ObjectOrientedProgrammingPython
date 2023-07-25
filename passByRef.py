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
    print(id(car))

feature(ford, "Audi")

print(id(ford))

print(ford.name)

# Main takeaway from this set of code is the changes we make to a object through other functions or any other ways also changes the object's property/attribute and the object's memory location or reference id does not change

# this is called mutatble object as after changing an object it's reference id or memory location still hasn't changed
# list and dictionary is mutable
# tuple is immutable