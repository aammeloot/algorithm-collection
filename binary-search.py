# Binary search

# If the file is there the code below should generate the following list of 100 numbers:
# [4, 14, 20, 30, 33, 62, 93, 102, 106, 109, 112, 116, 122, 124, 130, 132, 
# 132, 135, 147, 156, 159, 167, 193, 203, 211, 220, 227, 227, 258, 271, 290,
#  290, 317, 341, 350, 376, 398, 401, 404, 405, 410, 421, 423, 460, 461, 470,
#  473, 478, 505, 505, 514, 518, 545, 557, 568, 581, 591, 619, 623, 625, 636, 
# 641, 643, 650, 672, 680, 682, 706, 709, 724, 741, 744, 762, 766, 770, 772, 
# 781, 798, 801, 806, 807, 822, 824, 824, 826, 830, 869, 880, 887, 897, 906, 
# 917, 918, 926, 939, 947, 953, 955, 960, 980]

# Reading the numbers from the numbers.txt file
f = open("numbers.txt")
# Making it a list of strings
number_strings = f.readlines()
numbers = []
# Convert all to numbers and build number list
for n in number_strings:
    n = int(n)
    numbers.append(n)
# Sort numbers for binary search
numbers = sorted(numbers)
print(numbers)
print(numbers[50])

# Binary search: input validation
item = int(input("Please enter a number between 1 and 1000"))
while item < 1 or item > 1000:
    item = int(input("Please enter a number between 1 and 1000"))

# Set boundaries of search space
l = 0
r = len(numbers) - 1
found = False

# Loop
while not found:
    print("Search space index", l, "to", r)
    if r - l > 0: # if search space is greater than 1
        m = (r - l) // 2 # Roughly the middle of the search space
        print(l+m)
        if numbers[l + m] == item:
            found = True
        elif numbers[l+m] < item:
            l = l+m+1
        else:
            r = r-m-1
    else:
        if numbers[l] == item:
            found = True
        break

if found:
    print("Item found")
else:
    print("item not found")