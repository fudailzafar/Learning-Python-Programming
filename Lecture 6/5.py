# WAF to determine whether a number is even or odd.

num = int(input("Enter a number: "))

def even_odd(n):
    if(n%2==0):
        print("EVEN")
    else:
        print("ODD")

even_odd(num)