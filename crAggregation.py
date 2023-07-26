class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_profile(self, new_name, new_city, new_pin):
        self.name = new_name
        self.address.change_address(new_city, new_pin)

class Address:
    def __init__(self, city, pincode):
        self.city = city
        self.pincode = pincode

    def change_address(self, new_city, new_pin):
        self.city = new_city
        self.pincode = new_pin

add = Address("Dhaka", 344532)

cust = Customer("DingDong", "Male", add)

cust.name
cust.address.city
cust.address.pincode
cust.gender

cust.edit_profile("DongDing", "Khulna", 213213)
cust.name
add.city
add.pincode