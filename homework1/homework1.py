# File: homework1.py

# --- 2. Variables and Data Types ---

a = 2
print(a)
print(type(a)) # int – whole number without decimals

b = 1.5
print(b)
print(type(b))  # float – number with decimals

c = 3j
print(c)
print(type(c))  # complex number (real + imaginary)

d = "hello"
print(d)
print(type(d))  # str – string of characters (text)

e = ["apple", "banana", "cherry"]
print(e)
print(type(e))  # list – ordered collection of items, mutable

f = [1, 2, 3]
print(f)
print(type(f))  # list – another list, same type as e

g = (4, 6)
print(g)
print(type(g))  # tuple – ordered collection, immutable

h = {"name": "Ellen", "age": 20}
print(h)
print(type(h))  # dict – dictionary of key-value pairs

i = True
print(i)
print(type(i))  # bool – Boolean value

j = None
print(j)
print(type(j))  # NoneType – represents "nothing" or "null"

k = str(14)
print(k)
print(type(k))  # str – string (converted from int)

l = 1e4
print(l)
print(type(l))  # float – scientific notation, equals 10000.0

# Questions
# 1. How many different data types did you find? 
    # 9 (int, float, complex, str, list, tuple, dict, bool, NoneType)
# 2. What variables had the same datatype? 
    # e and f (both lists), d and k (both strings)
# 3. m = {1, 2, 3}, set – unordered collection of unique values
m = {1, 2, 3}
print(m)
print(type(m))  # set – collection of unique elements

# --- 2.2 Booleans ---

print(10 > 9)          # True
print(10 == 9)         # False
print(10 < 9)          # False
print(bool("abc"))     # True – non-empty string
print(bool(123))       # True – non-zero number
print(bool(["apple", "cherry", "banana"]))  # True – non-empty list
print(bool(False))     # False
print(bool(None))      # False
print(bool(0))         # False
print(bool(""))        # False – empty string
print(bool(()))        # False – empty tuple
print(bool([]))        # False – empty list
print(bool({}))        # False – empty dictionary
print(True and True)   # True
print(True or False)   # True
print(1 >= 2)          # False

# Questions
# 1. Boolean: a type that represents either True or False
# 2. Pattern: "Falsy" values like 0, "", [], {}, None is False; everything else is True
# 3. True expression: 5 != 6
# 4. False expression: 4 == 4 and 5 < 3

# --- 2.3 Operators ---

# Arithmetic
print(10 + 5)    # 15, addition
print(10 - 5)    # 5, subtraction
print(2 * 4)     # 8, multiplication
print(6 / 3)     # 2.0, division (always returns float)
print(5 % 2)     # 1, modulus (remainder)
print(3 ** 2)    # 9, exponentiation (3 squared)
print(15 // 2)   # 7, floor division (drops remainder)

# Assignment
x = 2
x += 4
print(x)  # 6, addition

x = 2
x -= 1
print(x)  # 1, subtraction

x = 2
x *= 3
print(x)  # 6, multiplication

x = 2
x /= 3
print(x)  # 0.666..., division

x = 2
x %= 3
print(x)  # 2, remainder

x = 2
x //= 3
print(x)  # 0, floor division

x = 2
x **= 3
print(x)  # 8, exponentiation

# Comparison
x = 2
y = 5
print(x == y)   # False, 2 does not equal 5
print(x != y)   # True, 2 does not equal 5
print(x > y)    # False, 2 is not greater than 5
print(x < y)    # True – 2 is less than 5

# Logical 
x = 4
print(x < 5 and x < 10)  # True
print(x < 5 and x < 3)   # False
print(x < 5 or x < 10)   # True
print(x < 5 or x < 3)    # True
print(not(x < 5 and x < 10))  # False

# Questions
# 1. / = float division, // = floor division
# 2. % gives remainder, // gives whole number result of division
# 3. % operator. Example: 10 % 3 = 1
# 4. and = both must be true; or = at least one must be true; not = inverts result

# --- 2.4 Strings ---
my_string = "hello"

print(my_string)  # hello
print(my_string[0])  # h
print(my_string[1])  # e
print(my_string[2])  # l
print(my_string[3])  # l
print(my_string[4])  # o
print(my_string[-1])  # o – last character
print(my_string[1:3])  # el – characters at index 1 and 2 (excludes index 3)
print(len(my_string))  # 5
print(my_string + "goodbye")  # hellogoodbye
print(my_string * 7)  # hellohellohellohellohellohellohello

# Questions
# 1. Slicing: extracting a portion of a string using [start:end] notation
# 2. # 2. Sliced strings: my_string[1:3] uses slice syntax; my_string[-1] uses negative indexing (a type of slicing)
# 3. 
name = "Oski"
print("Hello, my name is", name)  # Hello, my name is Oski
print(f"Hello, my name is {name}")  # Hello, my name is Oski

# --- 2.5 Terminal Commands ---
# 1. cd — Change Directory
# Moves you into a different folder
# cd homework1
# "I used cd to move into my homework1 directory."

# 2. ls — List Directory Contents
# ls
# "I used ls to see the files inside my current folder."

# 3. ls -a — List All (including hidden files)
# ls -a
# "I used ls -a to show hidden files (like .git or .DS_Store)."

# 4. mkdir — Make Directory
# mkdir test_folder
# "I used mkdir to create a folder called test_folder."

# 5. cat — Concatenate and Display File Contents
# cat homework1.py
# "I used cat to display the contents of my Python script."

# 6. pwd — Print Working Directory
# pwd
# "I used pwd to check which folder I was in."

# 7. cd .. — Move Up One Directory
# cd ..
# "I used cd .. to go up to the parent directory."

# 8. cd . — Stay in the Current Directory
# cd .
# "I used cd . but it just kept me in the same place."

# 9. cd ~ — Go to Home Directory
# cd ~
# "I used cd ~ to go to my home folder (e.g., /Users/myname)."

# 10. cp — Copy Files or Folders
# cp homework1.py backup_homework1.py
# "I used cp to make a copy of my script."

# 11. mv — Move or Rename Files
# mv oldname.py newname.py
# "I used mv to rename a file."

# 12. rm — Remove (Delete) Files
# rm test.txt
# "I used rm to delete a test file. Be careful!"

# 13. clear — Clear Terminal Screen
# clear
# "I used clear to clear the terminal screen for a fresh view."

# 14. grep — Search Text for a Pattern
# grep "hello" homework1.py
# "I used grep to search for the word 'hello' in my script."

# Questions:
# 1.
# touch — create a new, empty file
# touch notes.txt
# "Creates a blank file called notes.txt"

# echo — display text in terminal
# echo "Hello!"
# "Prints text to the terminal"

# head — show the first few lines of a file
# head homework1.py
# "Displays the first 10 lines of a file"

# 2. ls shows only regular (non-hidden) files, ls -a includes hidden files and directories (those starting with a dot, like `.git`).

# 3.
# ls -l — long format (shows file size, permissions, timestamps)

# cp -r — recursive copy (for folders)
# cp -r my_folder/ my_folder_backup/

# rm -i — interactive remove (asks before deleting)
# rm -i test.txt