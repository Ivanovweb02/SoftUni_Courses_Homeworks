count_of_number = int(input())
left_sum = 0
right_sum = 0

for number in range(count_of_number * 2):
    current_number = int(input())
    if number < count_of_number:
        left_sum += current_number
    else:
        right_sum += current_number

if right_sum == left_sum:
    print(f"Yes, sum = {left_sum}")
else:
    difference = abs(right_sum - left_sum)
    print(f"No, diff = {difference}")
