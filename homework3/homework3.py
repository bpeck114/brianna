# File: homework3.py

# --- 2.1 Say Goodbye ---
def say_goodbye(name):
    print("Goodbye,", name)

# --- 2.2 Area of a Circle ---
def area_of_circle(radius):
    area = 3.14 * radius ** 2
    print(f"The area of a circle with radius {radius} is {area}")

# --- 3.1 Subtract, Multiply, and Divide ---
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# --- 4.1 What Should I Wear? ---
def min_max_temp(temps):
    return (min(temps), max(temps))

# --- 4.2 Check if It’s the Weekend ---
def is_weekend_by_num(day_num):
    return day_num == 6 or day_num == 7

# --- 4.3 Fuel Efficiency Calculator ---
def fuel_efficiency(miles, gallons):
    if gallons == 0:
        return "Cannot divide by zero"
    return miles / gallons

# --- 4.4 Secret Code ---
def encrypt_number(n):
    last_digit = n % 10
    rest = n // 10
    digits = len(str(rest))
    return last_digit * (10 ** digits) + rest

# --- 5.1 Oski Stole Your Power ---
def power(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result

# --- 5.2.1 Min & Max with For Loops ---
def find_min_for(nums):
    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num
    return smallest

def find_max_for(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest

# --- 5.2.2 Min & Max with While Loops ---
def find_min_while(nums):
    i = 0
    smallest = nums[0]
    while i < len(nums):
        if nums[i] < smallest:
            smallest = nums[i]
        i += 1
    return smallest

def find_max_while(nums):
    i = 0
    largest = nums[0]
    while i < len(nums):
        if nums[i] > largest:
            largest = nums[i]
        i += 1
    return largest

# --- 5.3 Calculate the Sum ---
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

# --- 6. VS Code Test Run Example ---
# Example function test at the bottom of the file:
x = 2
y = 3
result = power(x, y)
print(f"The result of Oski Stole Your Power (5.1) with x = {x} and y = {y} is {result}.")