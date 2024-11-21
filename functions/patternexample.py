#Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
#*
#**
#***

def print_pattern(number):
    """
    Prints a pattern of stars based on the input number.
    """
    for i in range(1, number + 1):  # Loop from 1 to 'number' (inclusive)
        print('*' * i)  # Print '*' repeated 'i' times

print_pattern(3)

