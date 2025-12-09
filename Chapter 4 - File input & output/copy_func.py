# code to make copy of file

with open("file.txt", "r") as f:
    content = f.read()

with open("file_copy.txt", "w") as f:
    f.write(content)