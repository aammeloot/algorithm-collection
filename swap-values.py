# Swap two values.

# Method 1 - traditional
a = 5
b = 7
print(a,b)

# Swap them - create a third variable
c = b
b = a
a = c
print(a,b)

# Method 2 - Python way
i = "Alice"
j = "Bob"
print(i, j)

i, j = j, i # Swap them - Python way
print(i,j)