n = int(input("Enter a number for factorial :"))
def fact(n):
    if n < 2:
        return 1
    else :
        return n * (fact(n-1))
result = fact(n)
print(f"Factorial of number is :{result}")