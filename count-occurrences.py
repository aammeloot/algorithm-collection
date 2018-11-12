# Counting occurrences
# How many times a term appears in a list

# Create a list of terms
usernames = ["neil", "emily", "scott", "emily", "scott", "emily", "scott", "neil","neil","neil","neil","neil","neil","neil","neil","neil","neil","scott", "emily","neil","neil","neil","neil", "emily", "scott"]

search_term = "neil" # We will count "neil"
count = 0

# Go through all usernames
for e in usernames:
    if e == search_term:
        count += 1

print(search_term, "appears", count, "times.")