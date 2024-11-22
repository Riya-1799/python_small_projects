class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"ID: {self.id} \nName: {self.name}")

# Create an Employee object
emp = Employee(1, "Riya")
emp.display()

# Deleting the `id` property of the object
del emp.id

# Trying to access `id` after deletion with proper error handling
try:
    print(emp.id)
except AttributeError:
    print("The 'id' attribute has been deleted.")

# Delete the entire object
del emp

# Trying to access the deleted object
try:
    print(emp)
except NameError:
    print("The 'emp' object has been deleted.")
