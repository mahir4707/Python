# Function to remove any word from list and strip it at the same time 

def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Mahir", "Shahid", "Arman", "an"]

print(rem(l, "an"))
