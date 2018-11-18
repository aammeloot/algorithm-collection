# Reading example

# Read the whole file 
f = open("text1.txt")  # Open a text file in default read mode
text_content = f.read() # Read the whole file and store in a variable
print(text_content) # Print the whole text to screen
f.close() # Close the file

# Read line by line
f = open("text1.txt")
print()
print("First 4 lines:")
print()
for n in range(4): # Repeat 4 times
    print(f.readline()) # Print current line and move on to next
f.close()

# Create a list with all lines
f = open("text1.txt")
all_lines = f.readlines() # Read all lines and save in a list
f.close()

print(all_lines) # print the list of lines