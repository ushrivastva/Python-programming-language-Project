#  Shopping Cart Proggram

foods = []
prices = []
total =  0

while True:
    food = input("Enter food to cart or ('q' to quit): ").upper()

    if food.lower() == 'q':
        break

    else:
        foods.append(food)
        price = float(input(f"Enter the price of {food} in $: "))
        prices.append(price)
print("------------YOUR CART---------------")
print("Items:              Price('$')")
print("------              ----------")
for items,rate in zip(foods,prices):
               
    print(f"{items:10}:              {rate}")
    pr_price = int(rate)
    total += pr_price
print("-----------------------------------")
print(f"Total        =       {total}$")