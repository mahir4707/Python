# Code to read the file and find out whether it contains word "Twinkle" 

st = "twinkle"

f = open("file.txt")
data = f.read()

if st in data:
    print("Yes word is present in the file")
else:
    print("No word found in file")