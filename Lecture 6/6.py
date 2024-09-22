# Write a recursive function to calculate the sum of first n natural numbers.
num = int(input("Enter a number: "))

def sum(n):
    if n==0:
        return 0
    return n + sum(n-1)

final = sum(num)
print("Sum of all numbers from 0 to",num,"is:",final)
