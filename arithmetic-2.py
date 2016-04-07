#new arithmetic file --takes multiple inputs

def add(list_of_numbers):
    """ This a list of numbers and return their sum. 
    """

    #iterate over list w/ for loop add each element to the sum variable
    for index in range(len(list_of_numbers)):
        if index == 0:
            total = list_of_numbers[index]
        else: 
            total += list_of_numbers[index]
    return total

def subtract(list_of_numbers):
    """ This list and substracts them from each other.
    """

    for index in range(len(list_of_numbers)):
        if index == 0:
            total = list_of_numbers[index]
        else: 
            total -= list_of_numbers[index]
    return total

def multiply(num1, num2):
    """ This takes two numbers and returns the result of multiply them.
    """
    return num1 * num2

def divide(num1, num2):
    """ This takes two numbers and divides them and returns the total.
    """
    return num1 / num2

def square(num1):
    """ This take a number and returns it's square
    """
    return num1 * num1

def cube(num1):
    """ This take a number and returns it's cube
    """
    return num1*num1*num1

def power(num1, num2):
    """ This returns the first number raised to the power of the second number."""
    #print num2, "this is num 2"
    return num1 ** num2

def mod(num1, num2):
    """ Returns the remaider of first number divided by second number.
    """
    return num1 % num2

bunch_of_nums = [5, 2]
print add(bunch_of_nums)
print subtract(bunch_of_nums)