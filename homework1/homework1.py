# File: homework1.py

# --- Variables and Data Types ---
a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a float, a number with decimals

c = 3j
print(c)
print(type(c)) # c is a complex number, it contains real and imaginary parts

d = "hello"
print(d)
print(type(d)) # d is a string, it stores text

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, it contains multiple values (which are ordered and mutable)

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, it stores information with key-value pairs

g = (1, 2)
print(g)
print(type(g)) # g is a tuple, it's like a list but cannot be changed

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is also a list, but it only has strings

i = True
print(i)
print(type(i)) # i is a boolean, it is either True or False

j = None
print(j)
print(type(j)) # j is a NoneType, is represents "nothing"

k = [True, "blue", 12]
print(k)
print(type(k)) # k is another list, but it has mixed data types

l = str(14)
print(l)
print(type(l)) # l is a string, but it was an integer turned into a string

m = 1e4
print(m)
print(type(m)) # m is a float, it was written in scientific notation (1e4 = 10000.0)

# Questions:
# 1) I found 9 data types.
# 2) Integer, float, complex, string, list, dictionary, tuple, boolean, NoneType
# 3) b and m were both floats. d and l were both strings. e, h, and k were all lists.
# 4) l was a string. It was converted to a string with str(). str() converts data types to strings.
# 5) 
import numpy as np
n = np.array([1])
print(n)
print(type(n)) # n is a numpy.ndarray, its like a list but works better for mathematical operations


# --- Booleans ---
print(10 > 9)           # True, 10 is greater than 9
print(10 == 9)          # False, 10 is not equal to 9
print(10 < 9)           # False, 10 is not less than 9

print(bool("abc"))       # True, non-empty strings are True
print(bool(123))         # True, any non-zero number is True
print(bool(["apple", "cherry", "banana"]))  # True, non-empty list is True

print(bool(True))        # True, as stated
print(bool(False))       # False, as stated

print(bool(0))           # False, 0 is considered False in Python
print(bool(""))          # False, empty string is False
print(bool(" "), 4)      # True, a non-empty string is True
print(bool(()))          # False, empty tuple is False
print(bool([]))          # False, empty list is False
print(bool({}))          # False, empty dictionary is False

print(bool(True and False))     # False, because one is False
print(bool(True and True))      # True, both are True
print(bool(False and False))    # False, both are False

print(bool(True or False))      # True, at least one is True
print(bool(True or True))       # True, both are True
print(bool(False or False))     # False, neither is True

print(bool(not(False)))         # True, not False is True
print(bool(not(True)))          # False, not True is False

# Questions:
# 1) If a value is non-empty or non-zero if will return True. Otherwise, it returns False.
# 2) print(bool(" ")) because it looks empty, but a space makes it True
# 3) 
print(bool(5)) # True, a non-zero number is True
# 4) 
print(bool(None)) # False, None represents nothing 

# --- Operators ---
# Arithmetic Operators
print(10 + 5)     # 15, + performs addition
print(10 - 5)     # 5, - performs subtraction
print(2 * 4)      # 8, * performs multiplication
print(6 / 3)      # 2.0, / performs division and returns a float
print(5 % 2)      # 1, % gives the remainder
print(3 ** 2)     # 9, ** raises to the power (3 squared)

# Comparison Operators
print(5 == 2)     # False, 5 is not equal to 2
print(10 != 10)   # False, 10 is equal to 10
print(2 < 5)      # True, 2 is less than 5
print(12 > 5)     # True, 12 is greater than 5
print(5 <= 6)     # True, 5 is less than or equal to 6
print(1 >= 10)    # False, 1 is not greater than or equal to 10

# Assignment Operators
x = 5
x += 5
print(x)          # 10, adds 5 to x

x -= 4
print(x)          # 6, subtracts 4 from x

x *= 3
print(x)          # 18, multiplies x by 3

# Logical Operators
# 1) It returns True only if both conditions are True.

print(True and True)    # True
print(True and False)   # False

# 2) It returns True if at least one condition is True.

print(True or False)    # True
print(False or False)   # False

# 3) It reverses the boolean value.

print(not False)        # True
print(not True)         # False

# More Questions
# 1) / is regular divison, it always returns a float. // is floor divsion, it gives the whole number and drops decimals
# 2) % is the remainder of the divison. // gives the whole number result
# 3) I would use % to find the remainder. 
print(13 % 5) # This would return 2 because that's the remainder
# 4) Assignment operators work by storing or updating the value of a variable.

# --- Strings ---
my_string = "hello"

print(my_string)        # Prints: hello 
print(my_string[0])     # Prints: h, the first character (index 0)
print(my_string[1])     # Prints: e, the second character
print(my_string[2])     # Prints: l, the third character
print(my_string[3])     # Prints: l, the fourth character
print(my_string[4])     # Prints: o, the fifth character (last one in a 5-letter word)

print(my_string[-1])    # Prints: o, the last character using negative index

print(my_string[1:3])   # Prints: el, it slices from index 1 to 2 (3 is not included)

print(my_string[0:5:2]) # Prints: hlo, it started at h, stopped at o (exclusive), printed every other letter so hlo

print(len(my_string))   # Prints: 5, the length of the string

print(my_string + "goodbye")  # Prints: hellogoodbye, string concatenation

print(my_string * 7)    # Prints: hellohellohellohellohellohellohello, repeats string 7 times

# Questions:
# 1) Slicing means to select a portion of your string, [start:end], where end is exclusive
# 2) Uses regular print statement, seperates information with commas, automatically adds a space
name = "Oski"
print("Hello, my name is", name)

# 3) Uses an f-string which allows you to immediately insert variables inside your string with curly brackets {}
name = "Oski"
print(f"Hello, my name is {name}")

# 4) The first statement used string concatentation with commas and the second used f-strings.

# --- Commands ---
# cd
# Changes directories. Use it to move from one folder to another.
# Example: cd Desktop

# ls
# Lists files and folders in the current directory.
# Example: ls

# ls -a
# Lists all files, including hidden files (those starting with a dot).
# Example: ls -a

# mkdir
# Makes a new folder (directory).
# Example: mkdir my_folder

# cat
# Displays the contents of a file.
# Example: cat notes.txt

# pwd
# Prints the current directory path (where you are right now).
# Example: pwd

# cd ..
# Moves up one level to the parent directory.
# Example: cd ..

# cd .
# Refers to the current directory (no change in location).
# Example: cd .

# cd ~
# Takes you to your home directory.
# Example: cd ~

# cp
# Copies a file or folder.
# Example: cp file1.txt copy.txt

# mv
# Moves or renames a file or folder.
# Example: mv oldname.txt newname.txt

# rm
# Deletes a file.
# Example: rm file.txt

# clear
# Clears the terminal screen.
# Example: clear

# grep
# Searches for matching text inside files or output.
# Example: grep "apple" shopping_list.txt

# Questions:
# 1) whoami, prints the username of the person currently logged in
# man ls, opens the manual or help page on the terminal
# date, prints the current date and time (with the proper timezone!)

# 2) ls only shows visible files and folders, ls -a shows hidden ones

# 3) A hidden file is a file that doesn't show up by default. Starting with a period .
# Usually they are files that contain settings, preferences and system information.
# Like .git! Which we will learn next class :)

# 4) ls -l, shows detailed information about each file
# cp -r python_decal_fa25, copies all subdirectories in a directory as well
# rm -r python_decal_fa25, removes all subdirectories in a directory as well

