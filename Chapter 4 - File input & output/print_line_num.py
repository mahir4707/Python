# code to print line no where word given is present in file

with open("log.html", "r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("powerful" in line):
        print(f"Yes line is present. Line no:{lineno}")
        break
    lineno += 1

else:
    print("No line is not present")