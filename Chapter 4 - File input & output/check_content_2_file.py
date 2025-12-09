# Code to check the contents of two file same or not

with open("2_file.txt", "r") as f:
    content1 = f.read()

with open("1_file_copy.txt", "r") as f:
    content2 = f.read()

if(content1 == content2):
    print("Content are same")
else:
    print("No these files are not same")