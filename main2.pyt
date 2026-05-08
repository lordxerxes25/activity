num_pizzas = int(input("How many pizzas are ordered? "))
total_bill = num_pizzas * 249
print("Total bill is: ₹", total_bill)
money_collected = int(input("Enter total money collected from all friends: ₹"))
if money_collected == total_bill:
    print("Money collected is exactly enough")
if money_collected > total_bill:
    print("They have extra money")
else:
    print("They need more money")
h=total_bill - money_collected
k=money_collected - total_bill
if total_bill > money_collected:
    print(h,"is the money they need more")
else:
    print(k,"is extra money")