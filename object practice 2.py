class Person:
    def __init__(self, name, age):
        self.name = name    # This is an instance variable
        self.age = age
person1 = Person("Ayan", 25)
person2 = Person("Bobby", 30)
print(person1.name)
print(person2.age)