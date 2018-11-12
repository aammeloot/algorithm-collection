# Linear search - iterates through all the elements
# of a list until the search term has been found or
# the list has been depleted

# Create a list of names
names = ["Neil", "Scott", "Peter", "Aurelien", "Jim"]

# Enter a name
n = input("Please enter a name to search")
index = 0 # Position of the element found

# Linear search -- traditional
found = False # 'found' flag
for i in range(len(names)):
    e = names[i] # Take current element
    if e == n: # If it matches the search term
        found = True
        index = i # Position where found
        break

if found:
    print("Element found at index", index)
else:
    print("Element not found")




# Similar search - using Python shortcuts
# No guarantee it is linear
found = False
if n in names:
    print("Element in list")
else:
    print("Element not in list")
