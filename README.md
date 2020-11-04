# Python Functions
- functions are used to reduce / eliminate DRY (Don't Repeat Yourself)
## What Are Functions and Why Are They Used?
- functions are used to bundle sets of instructions that are used multiple times.
## How To Create a Function
- The following syntax is used to create a function```def <function_name>(arg1,arg2... argN):``` 
- Examples: 
```
# create a new function that takes 2 arguments as ints and adds the value of the two args
def add(num1, num2):
    print("The answer is", (num1 + num2))


add(2, 5)


# create a function that subtracts the two values that are given
def subtract(num1, num2):
    print("The answer is", (num1 - num2)


subtract(2, 5)


# create a function that multiplies two args
def multiply(num1, num2):
    print("The answer is", (num1 * num2)


multiply(2, 5)


# create a function that divides two args
def division(num1, num2):
    print("The answer is", (num1 / num2)


division(2, 5)


# create a function that calculates % of two args
def modulus(num1, num2):
    print("The answer is", (num1 % num2)


modulus(5, 2)


# create a function that adds two args using return
def addition(num1, num2):
    answer = num1 + num2
    return answer


x = addition(5, 2)
print(f"The answer is {x}")
```
## Using return statements:
```
# create a function that multiplies two args
def multiply(num1, num2):
    return num1 * num2


print(multiply(2, 5))


# create a function that divides two args
def division(num1, num2):
    return num1 / num2


print(division(2, 5))


# create a function that calculates % of two args
def modulus(num1, num2):
    return num1 % num2


print(modulus(5, 2))
```
## Best Practices
- Return statements are used to return the result of any function \
Examples :
```
def modulus(num1, num2):
    return num1 % num2

print(modulus(num1, num2))
```
here the modulus value of num1 and num2 are returned so it can be printed
 - Don't have DRY code
 - Have small blocks of code in any function that does one job
 - Pseudo coding will help code to be understood (1 line explanation)
 - HINTs: Create hints in simple bullet points or pointers
 - Comments regarding your function results
 - KISS (Keep It Simple Stupid)