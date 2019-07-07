class RobbysFamily():

    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def print_age_name_occupation(self):
        print("My name is " + self.name + " and I'm " + str(self.age) + " old " + self.occupation)

member1 = RobbysFamily("Robert", 40, "IT engineer")

member1.print_age_name_occupation()
