
words = ["Diamond", "earth"]


with open("2_file.txt", "r") as f:
    content = f.read()

for word in words:

    content = content.replace(word, "#"*len(word))

with open("2_file.txt", "w") as f:
    f.write(content)