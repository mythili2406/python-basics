
    
'''Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.


'''
n=int(input("enter a number:"))
def get_factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive call
    return n * get_factorial(n - 1)

print(f"factorial of {n} is : {get_factorial(n)}")  # Output: 120
