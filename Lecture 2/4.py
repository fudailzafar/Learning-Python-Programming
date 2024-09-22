# WAP to find the greatest of 3 numbers entered by the user.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter the third number: "))

if(num1>=num2):
    if(num1>=num3):
        print("Greatest number is:", num1)
    else:
        print("Greatest number is:", num3)
else:
    print("Greatest number is:", num2)