# Writing text to a file
# Practical example

# Writing a single line to a file
f = open("text-1.txt", "w") # Open or create text file if it doesn't exist in "write" mode
f.write("Hello World") # Write text into the file
f.close() # Close the file, this is important as it will commit all the text to file.

# Writing a number of lines to the text file
f = open("text-2.txt", "w")
for i in range(1,11):  #Write multiple lines in the file
    f.write("This is line " + str(i) + "\n") # '\n' is a special character that represents a line break
f.close() # Do not forget to close the file

# Append text to an existing text file
f = open("text-2.txt", "a") # 'a' mode means we add to the file
f.write("And this is a bonus line...")
f.close()