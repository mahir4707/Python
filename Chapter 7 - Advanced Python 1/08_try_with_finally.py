# finally block executes no matter what, whether an exception occurred or not

try:
    file = open("data.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing file...")
