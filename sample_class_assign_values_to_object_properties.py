#class is a template - like a cookie cutter
class RobbysFamily():

#Use the __init__() function to assign values to object properties, or
#other operations that are necessary to do when the object is being created
#The self parameter is a reference to the current instance of the class,
#and is used to access variables that belongs to the class.
#It does not have to be named self , you can call it whatever you like,
#but it has to be the first parameter of any function in the class

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello_to_family_member(self):
        print("Hey " + self.name + " you are " + str(self.age))

#Below we are creating new objects called "member1" and "member2"
member1 = RobbysFamily("Robby", 40)
member2 = RobbysFamily("Indra", 37)

member1.say_hello_to_family_member()
member2.say_hello_to_family_member()
