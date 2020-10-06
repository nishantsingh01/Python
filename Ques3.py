def factorial(a):
    if a <= 1:
        return 1
    return a*factorial(a-1)

# Fibonacci function to find nth term of series
def fib(a): #Recursive
    if a <= 0:
        return 0
    if a == 1:
        return 1
    return fib(a-1) + fib(a-2)

if __name__ == "__main__":
    num =  int(input("Enter a number: "))
    print("{}th term of fibonacci series: ".format(num), fib(num))
    print("Factorial of {}: ".format(num), factorial(num))
