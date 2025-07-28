# File: homework4.py

# --- Lists ---

# List Operations
foods = ["pizza", "sushi", "ramen", "ice cream", "burgers"]

print(foods[1])  # sushi
print(foods[-1])  # burgers
foods.append("tacos")
foods.insert(0, "apple")
del foods[2]
print(len(foods))

for food in foods:
    print(food.upper())

ends = [foods[0], foods[-1]]
print(ends)

if "potato" in foods:
    print("A potato!")
else:
    print("No potato!")

# Slicing and Striding
numbers = list(range(0, 21))

def get_first_15(lst):
    return lst[:15]

def get_every_5th(lst):
    return lst[::5]

def reverse_and_stride(lst):
    return lst[::-1][::3]

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

print("Final result:", step3)


# Nested Lists
# Nested List Operations

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[2])  # [7, 8, 9]
print(numbers[1][1])  # 5
numbers.append([10, 11, 12])

def sum_nested(lst):
    total = 0
    for row in lst:
        for num in row:
            total += num
    return total

print("Total sum:", sum_nested(numbers))

# Create a 5x5 List
def create_5x5():
    grid = []
    count = 1
    for _ in range(5):
        row = []
        for _ in range(5):
            row.append(count)
            count += 1
        grid.append(row)
    return grid

def replace_multiples_of_3(grid):
    new_grid = []
    for row in grid:
        new_row = ["?" if num % 3 == 0 else num for num in row]
        new_grid.append(new_row)
    return new_grid

def sum_non_question(grid):
    total = 0
    for row in grid:
        for val in row:
            if val != "?":
                total += val
    return total

# --- Dictionaries ---

# Dictionary Operations
ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"]) # 30
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]

for name, age in ages.items():
    print(f"{name} is {age} years old.")


# --- Debugging ---
# Random example. Students should have three of these throughout the code:
"""
my_list = [1, 2, 3]
print(my_list[3])

Error: IndexError: list index out of range
I tried to access index 3, but the list only has indices 0–2.
Fix: Changed the index to 2 or added a 4th element.
"""

grid_5x5 = create_5x5()
grid_with_q = replace_multiples_of_3(grid_5x5)
final_sum = sum_non_question(grid_with_q)

print("Grid:", grid_with_q)
print("Sum:", final_sum)