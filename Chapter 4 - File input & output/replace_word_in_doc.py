# Code to replace Diamond with #### in file 

word = "Diamond"

with open("2_file.txt", "r") as f:
    content = f.read()

    contentNew = content.replace(word, "#####")

with open("2_file.txt", "w") as f:
    f.write(contentNew)