from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(input().split())
functions = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b if b != 0 else 0
}

total_honey = 0
while working_bees and nectar:
    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()
    if current_nectar >= current_bee:
        current_symbol = symbols.popleft()
        total_honey += abs(functions[current_symbol](current_bee, current_nectar))
    else:
        working_bees.appendleft(current_bee)

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
