# lets create a greeting function

# Each function has a block of code to execute to ideally perform one task
# def greeting():
#     print("Welcome on board")

# nothing will happen as the function hasn't been called
# to call the function
# greeting()

# Adding arguments to the function
# def greeting(name):
#     print(f"Welcome on board {name.capitalize()}")
#
# greeting("dave") # to enable the function to run an argument must be given

# create a new function that takes 2 arguments as ints and adds the value of the two args
def add(num1, num2):
    print("The answer is", (num1 + num2))

add(2, 5)


# create a function that subtracts the two values that are given
def subtract(num1, num2):
    print("The answer is", (num1 - num2))


subtract(2, 5)


# create a function that multiplies two args
def multiply(num1, num2):
    return num1 * num2


multiply(2, 5)


# create a function that divides two args
def division(num1, num2):
    return num1 / num2


division(2, 5)


# create a function that calculates % of two args
def modulus(num1, num2):
    return num1 % num2


modulus(5, 2)


# create a function that adds two args using return
def addition(num1, num2):
    answer = num1 + num2
    return answer


x = addition(5, 2)
print(f"The answer is {x}")
