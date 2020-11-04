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
## Best Practices