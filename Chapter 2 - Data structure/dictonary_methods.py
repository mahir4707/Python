# code to write the whole directory item 

score = {
    "Team A" : 235,
    "Team B" : 198,
    "Team C" : 216
}

print(score.items())

# to get only keys
print(score.keys())

# to get only values
print(score.values())

# to update the dictonary
score.update({"Team B": 220, "Team A": 229})
print(score)

# using get function
print(score.get("Team A"))

# it returns none when using get function to find entry which is not in dictonary
print(score.get("Team xD"))

# returns error when finding entry which is not in dictonary
print(score["Team xD"])