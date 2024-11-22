expense = [2200, 2350, 2600, 2130, 2190]

#In Feb, how many dollars you spent extra compare to January?

extra_money = expense[1]-expense[0]
print(f"in feb they spent {extra_money} than January.")

#Find out your total expense in first quarter (first three months) of the year.

total_quarter = expense[0] + expense[1] + expense[2]
print(f"total expense of 1st quater is {total_quarter}")

#Find out if you spent exactly 2000 dollars in any month
found = False  # Flag to track if the condition is met
for i, amount in enumerate(expense):
    if amount == 2000:
        print(f"In month {i + 1}, they spent exactly 2000 dollars.")
        found = True

if not found:
    print("They did not spend 2000 dollars in any month.")

#June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

expense.append("1980")

#You returned an item that you bought in a month of April and
#got a refund of 200$. Make a correction to your monthly expense list
#based on this

expense[3]= 2130 - 200
print(expense)