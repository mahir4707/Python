# program to open three files and if not found then message without exiting the program must be printed prompting the same
try:
    with open("1.txt") as f:
        print("File 1 opened successfully.")
except FileNotFoundError as e:
    print(f"Error: {e}")

try:
    with open("2.txt") as f:
        print("File 2 opened successfully.")
except FileNotFoundError as e:
    print(f"Error: {e}")

try:
    with open("3.txt") as f:
        print("File 3 opened successfully.")

except FileNotFoundError as e:
    print(f"Error: {e}")