# WAF to find the factorial of n. (n is the parameter)

num = int(input("Enter a number: "))

def fact(n):
    fact = 1
    for i in range(1, num+1):
        fact*=i
    print(fact)

fact(num)