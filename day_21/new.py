#class
class Person:
    pass

print(Person)

#object
p = Person()
print(p)

#constructor
class Person:
    def __init__ (self, firstname, lastname, age, country, city):
        #self allows to attach parameter to the class
        self.firstname =firstname
        self.lastname =lastname
        self.age =age
        self.country =country
        self.city =city
    
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'


p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())

#constructor with default values to avoid errors
class Person:
    def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills= []

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
        
    def add_skill(self, skill):
        self.skills.append(skill)


p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
print(p1.skills)

p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())

#inheritance
class Student(Person):
    pass

s1= Student('adam', 'bakeer', 20, 'Jordan', 'amman')
print(s1.person_info())
s1.add_skill('html')
s1.add_skill('css')
print(s1.skills)

#overriding parent class
class Student(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age,country,city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)