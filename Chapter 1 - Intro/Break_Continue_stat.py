# Code to use the break, continue and pass statement 

# Break Statement
for i in range(50):
    if(i == 38):
        break # this will break the loop
    print(i)

# Continue Statement 
i=0
while(i<25):
    if(i == 16):
        i+=1
        continue # this will skip the iteration 16 and continue loop further
    print(i)
    i += 1

# pass statement
# -- considered as null and do nothing
for i in range(1, 40):
    pass # this will simply pass the loop without executing it