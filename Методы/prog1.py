from datetime import *

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def personeinfo(self):
        print(self.name)
        print(self.age)

    @staticmethod
    def personeage(person):
        return person.age >= 18

    @classmethod
    def newpersone(cls, age, today):
        cls(age, today().datetime())

