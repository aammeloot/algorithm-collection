# Bubble sort
# Go through all the elements of a list
# Check that two adjacent elements are in the right order
# Swap if necessary
# Move on
# Rinse
# Repeat
# If we go through the list an no swaps are required, then it's sorted

# Here is our non-sorted list:
numbers = [12, 5, 8, 6, 10, 3, 2, 15]
print(numbers)
# Flag indicating the list is sorted
# Default is false
is_sorted = False
# In a loop from the first to the penultimate element
limit = len(numbers) - 1

# First loop: conditional loop repeating as long
# as it isn't sorted
while not is_sorted:
    is_sorted = True # Assume it is sorted
    # Second loop: through all the elements of the
    # list except the last one
    for i in range(limit):
        # Sorting ascending so left should be <= right
        # If current number is greater than next one
        # (Wrong)
        if numbers[i] > numbers[i + 1]:
            # Swap the numbers
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            # If a swap was needed, then list wasn't sorted
            is_sorted = False

print(numbers)