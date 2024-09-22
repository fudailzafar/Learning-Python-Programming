# WAP to find the factorial of first n numbers. 

factorial = 1
n = int(input("Enter a number: "))

for i in range(1, n+1):
    factorial*=i

print("Factorial is:", factorial)