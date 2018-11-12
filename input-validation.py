# Input validation

# In this scenario enter an integer stricly between 1 and 10

n = int(input("Enter a number between 1 and 10"))
while n < 1 or n > 10:
    n = int(input("Enter a number between 1 and 10"))

print("Thank you")
