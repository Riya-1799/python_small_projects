#Write a program that asks user to enter a city name and it should tell which country the city belongs to

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input("enter the city name:")

if city in india:
    print(f"{city} is in india")
elif city in pakistan:
    print(f"{city} is in pakistan")
elif city in bangladesh:
    print(f"{city} is in bangladesh")
else:
    print(f"I won't able to give you the country of {city}, sorry for it")

city1 = input("enter the 1st city name:")
city2 = input("enter the 2nd city name:")

if city1 in india and city2 in india:
    print("both cities are in india")
elif city1 in pakistan and city2 in pakistan:
    print("both cities are in pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print("both cities are in bangladesh")
else:
    print("both cities are not belong to same country")

