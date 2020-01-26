class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def say_name(self):
        print('My name is ', self.name)

    def say_age(self):
        print('Age is ', self.age)

    def say_gender(self):
        print('Gender is ', self.gender)

p = Person('Thiha Tun', 22, "Male")
p.say_name()
p.say_age()
p.say_gender()
