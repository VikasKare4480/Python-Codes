
# pass statement  -- Only that block get skipped 

for i in range(10):

    if(i == 5):
        pass
    else:
        print(i)
    
    print("Hello")



# countinue statement -->> to next iteration


for i in range(10):

    if(i == 5):
        continue; 
    else:
        print(i)
    print("Hello")


