# WAP to print the greatest of 4 numbers.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

if(num1>=num2 and num1>=num3 and num1>=num4):
    print("Greatest number is:", num1)
elif(num2>=num3 and num2>=num4):
    print("Greatest number is:", num2)
elif(num3>=num4):
    print("Greatest number is:", num3)
else:
    print("Greatest number is:", num4)