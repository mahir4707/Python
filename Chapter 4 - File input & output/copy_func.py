# code to make copy of file

with open("2_file.txt", "r") as f:
    content = f.read()

with open("1_file_copy.txt", "w") as f:
    f.write(content)