# Concession stand program

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.00,
        "soda": 3.50,
        "lemonade": 4.25
}

cart = []
total = 0

print("---------MENU---------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-----------------------")

food = input("Enter food items from menu (q to quit): ").lower()
while True:
    if food in ["q","no"]:
        print()
        print()
        print("        ✨ Thank You! ✨       ")
        print()
        break
    elif menu.get(food) is not None:
        cart.append(food)
    food = input("       Are you want more items or (NO): ").lower()
    
        
print("------- YOUR ORDER ------")
for food in cart:
    total += menu.get(food)
    print(food)

print()
print("-------------------------")
print(f"Total is: ${total:.2f}")
print("-------------------------")