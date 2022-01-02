# OOP-model for a university: person module

class Person:

    # IMPORTANT EXAMPLE - component 1 of 2:
    person_count = 0  # create a class attribute and initialize it with 0
    instances = []

    def __init__(self, last_name, first_name, age):

        Person.instances.append(self)

        # IMPORTANT EXAMPLE - component 2 of 2:
        # When initialized, increase the counter on all objects of the person class!
        Person.person_count += 1  # by making it one part of each __init__ process

        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def __str__(self):
        """return some basic information about a given <Person> object"""
        return f"{self.first_name} {self.last_name}, age: {self.age}"

    @classmethod
    def search_instance_by_name(cls, search_key):
        """list comprehension for getting all instances by a search key
        Works for all classes inheriting from <Person> !"""
        return [obj for obj in cls.instances if (obj.last_name == search_key) or (obj.first_name == search_key)]
