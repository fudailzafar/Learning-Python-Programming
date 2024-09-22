# Search for a number x in this tuple using loop:

tuple = (1,4,9,16,25,36,49,64,81,100)

num = int(input("Enter your number: "))

for el in tuple:
    if(el == num):
        index = tuple.index(el)
        print("Index is", index)
