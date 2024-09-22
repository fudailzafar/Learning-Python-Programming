# Search for a number x in this tuple using loop:

tup = (1,4,9,16,25,36,49,64,81,100)

x = int(input("Enter the number: "))

i = 0
while(i<len(tup)):
    if(tup[i]==x):
        print("Found at index: ", i)
        break
    else: 
        print("finding...")
    i+=1

print("end of loop")