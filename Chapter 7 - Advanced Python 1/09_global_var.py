# global variable used when we dont want to change the value of variable inside function

a = 10 

def change():
    global a  #using global keyword to modify the global variable
    a = 20

change() #checks for local variable first if global is there it modifies that
print(a)  # Output: 10