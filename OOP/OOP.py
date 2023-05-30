#def main():
 #   get_person()

#def get_person():    
 #   name = input("What is your name?")
 #   country = input("Nationality?")
 #   print ("Hello (name) from(country)")

 #   return[name, country]



from typing_extensions import Self


class Person:
    def _int_(self, first_name, last_name, age):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

person1 = Person('John', 'Doe', 30)
print(person1)
