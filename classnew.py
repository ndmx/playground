from unicodedata import name


class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name)
    def __str__(self):
        return "Person's name is {}".format(self.name)

# Create a new instance with a name of your choice
some_person = Person("Alex")
# Call the greeting method
print(some_person.greeting())