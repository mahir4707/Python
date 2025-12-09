# Code to print multiplication table from 2 to 20 and print it in different file and place that file into different folder 

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {i*n}\n"
        
        with open(f"tables/table_{n}.txt", "w") as f:
            f.write(table)

for i in range(2, 21):
    generateTable(i)