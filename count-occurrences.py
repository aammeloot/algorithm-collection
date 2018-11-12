# Counting occurrences
# How many times a term appears in a list

# Create a list of terms
usernames = ["neil", "emily", "scott", "emily", "scott", "emily", "scott", "neil","neil","neil","neil","neil","neil","neil","neil","neil","neil","scott", "emily","neil","neil","neil","neil", "emily", "scott"]

search_term = "neil" # We will count "neil"
count = 0 # At first there is nothing found

# Go through all usernames
for e in usernames: # Iterate through the list
    if e == search_term: 
        count += 1 # If match add one to count

print(search_term, "appears", count, "times.")