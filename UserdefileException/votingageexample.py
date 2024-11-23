class MiniorException(Exception):
    pass
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def get_minior_age(self):
        if int(self.age) <= 18:
            raise MiniorException
        else:
            print(f"the age of {self.name} is {self.age}, can give their vote")

    def display(self):
        try:
            self.get_minior_age()
        except MiniorException:
            print(f"{self.name} is not an adult, cannot be vote")


# No exception
person("Bhavin", 17).display()

# AdultException is raised
person("Dhaval", 23).display()

