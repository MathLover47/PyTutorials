class Person:
                persons = 0
                def __init__(self, name, age):
                                self.name = name
                                self.age = age
                                global person
                                Person.persons += 1
                @staticmethod
                def get_persons():
                                return Person.persons

Person.get_Persons = staticmethod(Person.get_persons)

