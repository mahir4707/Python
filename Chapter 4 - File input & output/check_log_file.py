#Code to find word in log file 

with open("4_log.html", "r") as f:
    content = f.read()

if "Mahir" in content:
    print("Yes word is present")
else:
    print("No word is not present")