available_amount = float(input())
gender = input()
age = int(input())
sport = input()

price = 0

if gender == "m":
    if sport == "Gym":
        price = 42
    elif sport == "Boxing":
        price = 41
    elif sport == "Yoga":
        price = 45
    elif sport == "Zumba":
        price = 34
    elif sport == "Dances":
        price = 51
    elif sport == "Pilates":
        price = 39

elif gender == "f":
    if sport == "Gym":
        price = 35
    elif sport == "Boxing":
        price = 37
    elif sport == "Yoga":
        price = 42
    elif sport == "Zumba":
        price = 31
    elif sport == "Dances":
        price = 53
    elif sport == "Pilates":
        price = 37

if age <= 19:
    price -= price * 0.20

if available_amount >= price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    needed_money = price - available_amount
    print(f"You don't have enough money! You need ${needed_money :.2f} more.")
