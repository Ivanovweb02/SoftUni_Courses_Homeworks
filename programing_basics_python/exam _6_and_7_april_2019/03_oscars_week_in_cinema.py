movie_name = input()
hall_type = input()
bought_tickets = int(input())

tickets_price = 0

if movie_name == "A Star Is Born":
    if hall_type == "normal":
        tickets_price = 7.50
    elif hall_type == "luxury":
        tickets_price = 10.50
    elif hall_type == "ultra luxury":
        tickets_price = 13.50

elif movie_name == "Bohemian Rhapsody":
    if hall_type == "normal":
        tickets_price = 7.35
    elif hall_type == "luxury":
        tickets_price = 9.45
    elif hall_type == "ultra luxury":
        tickets_price = 12.75

elif movie_name == "Green Book":
    if hall_type == "normal":
        tickets_price = 8.15
    elif hall_type == "luxury":
        tickets_price = 10.25
    elif hall_type == "ultra luxury":
        tickets_price = 13.25

elif movie_name == "The Favourite":
    if hall_type == "normal":
        tickets_price = 8.75
    elif hall_type == "luxury":
        tickets_price = 11.55
    elif hall_type == "ultra luxury":
        tickets_price = 13.95

total_price = bought_tickets * tickets_price

print(f"{movie_name} -> {total_price :.2f} lv.")
