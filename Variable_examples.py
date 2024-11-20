#You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.

length = 92
width = 48.8


def football_ground_area(length, width):
    area = float(length * width)
    print(" area of football field is : " + str(area))


football_ground_area(length, width)

#You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave
# shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give
# you back?

num_of_chips = 9
price_of_chips = 1.49
total_price = num_of_chips * price_of_chips


def change_of_payment(Cashyougave, total_price):
    change = Cashyougave - total_price
    print("your change is : " + str(change))


change_of_payment(20, total_price)

#You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length.
# If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles.
# Calculate and print the cost using python

length = 5.5
area_of_bathroom = length**2
cost = 500
totalcost = area_of_bathroom * cost
print("total cost of bathroom is : " + str(totalcost))

## 4. Print binary representation of number 17

num = 17
print("binary of nuber 17 : " ,format(num, 'b'))
