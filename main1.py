name = input("What is your name? ")

age = int(input("How old are you? "))

if age < 5:
    print("You get free entry because you are under 5 years old. Enjoy the match!")
else:
    if age < 10:
        print("Sorry, you must be at least 10 years old to enter.")
    else:
        tickets = int(input("How many tickets do you want? "))

        print("Ticket types:")
        print("1. Regular ticket")
        print("2. VIP ticket (₹500 each)")
        ticket_type = input("Enter 1 for Regular or 2 for VIP: ")

        if ticket_type == "2":
            price = 500
        else:
            if age < 18:
                price = 100
            else:
                price = 250

        total = price * tickets

        if tickets > 4:
            discount = total * 0.10
            total = total - discount
            print(f"You got a 10% discount of ₹{discount:.2f}!")

        team = input("Which team do you support? ")
        print(f"Awesome! {team} fans are the best!")

        print(f"{name}, your total cost is ₹{total:.2f}. Enjoy the game!")
amount_paid = int(input("please enter the amount to pay for the tickets: ₹"))
if amount_paid == total:
    print("Payment successful! Enjoy the match!")
    print("have a great time")
else:
    print("Payment failed. Please try again.")
