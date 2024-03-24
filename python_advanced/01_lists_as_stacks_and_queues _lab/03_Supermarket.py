from collections import deque

customers_list = deque()
name = input()

while name != "End":
    if name == 'Paid':
        while customers_list:
            print(customers_list.popleft())
    else:
        customers_list.append(name)
    name = input()

print(f"{len(customers_list)} people remaining.")
