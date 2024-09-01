class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

    def add_skill(self, skill):
        self.skills.append(skill)

p = Person('Adam', 'Bakeer', 20, 'Jordan', 'Amman')
print(p.person_info())
p.add_skill('HTML')
p.add_skill('CSS')
print(p.skills)

class Student(Person):
    pass

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
print(s1.person_info)