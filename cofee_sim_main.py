DRINKS = {
    #drink: (price, water [ml], coffee [g], milk [ml])
    "espresso": (1.75, 50, 18, 0),
    "capuccino": (2.15, 200, 24, 150),
    "latte": (2.75, 250, 24, 100)
}

machine_resources = {
    "money $": 0,
    "water": 1000,
    "coffee": 100,
    "milk": 1000
}

order = [0, ""]

while True:
    print("What would you like for a drink?")
    print("Drink options: \n"
          "- Espresso: $1.75 \n"
          "- Capuccino: $2.15\n"
          "- Latte: $2.75")

    customer_choice = input()
    order[1] = customer_choice.lower()



    def payment(order, money):
        """Receive the payment from customer and check for the amount."""
        print(order[1], money)
        total_sum = money[0]*0.01 + money[1]*0.05 + money[2]*0.1 + money[3]*0.25
        order[0] += total_sum
        print(order[0], DRINKS[order[1]][0])
        if order[0] == DRINKS[order[1]][0]:
            print("Thank you, your drink is beeing prepared!")
            complete_order(order[1])
        elif order[0] > DRINKS[order[1]][0]:
            returning = round(order[0] - DRINKS[order[1]][0], 2)
            print(f"The provided sum is too much. Returning: ${returning}")
            complete_order(order)
        else:
            print("The provided sum is not enough.")
            print("Do you want to cancel or continue the order?")
            choice_ins_funds = input()
            if choice_ins_funds == "cancel":
                print("Good bye!")
            else:
                print("Please, provide the required sum for the drink: ")
                payment(order, payment_input())


    def payment_input():
        print("How many Pennies? ")
        penny = int(input())
        print("How many Nickels?")
        nickels = int(input())
        print("How many Dimes?")
        dime = int(input())
        print("How many Quarters?")
        quarter = int(input())
        return [penny, nickels, dime, quarter]


    def check_availability(order):
        """Check resource availability."""
        print(order)
        if DRINKS[order[1]][1] > machine_resources["water"] or DRINKS[order[1]][2] > machine_resources["coffee"] or DRINKS[order[1]][3] > machine_resources["milk"]:
            print("Sorry, there is not enough resources in the machine. Please, contact support.")
        else:
            print("Please, provide the required sum for the drink: ")
            payment(order, payment_input())


    def complete_order(order):
        """Remove the resources, add money to the bank and provide the drink."""

        order[0] = 0
        machine_resources["money $"] += DRINKS[order[1]][0]
        machine_resources["water"] -= DRINKS[order[1]][1]
        machine_resources["coffee"] -= DRINKS[order[1]][2]
        machine_resources["milk"] -= DRINKS[order[1]][3]
        print("Your coffe has been prepared. Enjoy.")

    if order[1] == "report":
        print(f"Money in the machine: ${machine_resources["money $"]}")
        print(f"Water in the machine: {machine_resources["water"]} [ml]")
        print(f"Coffee in the machine: {machine_resources["coffee"]} [g]")
        print(f"Milk in the machine: {machine_resources["milk"]} [ml]\n")

    else:
        check_availability(order)