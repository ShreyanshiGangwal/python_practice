# Use encapsulation (private variable)...

class Person:
    def __init__(self, name):
        self.__name = name          # Private variable

    def get_name(self):
        return self.__name
    
p = Person('Shreya')
print(p.get_name)