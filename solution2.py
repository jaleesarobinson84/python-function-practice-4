# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(numbers):
    # return the product of all the numbers in a list
    # Arguments:
    # numbers (list of int or float): list of numbers
    # Returns:
    # (int or float): the product of all the numbers in the list
    product = 1
    for num in numbers:
        product *= num
    return product

# the below code fragment can be found in:
my_list = [1, 2, 3, 4, 5]
print("result of multiplication", mult_list(my_list))