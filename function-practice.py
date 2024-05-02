def max_num(num1, num2, num3):
    # return the maximum of three numbers
    # Arguments:
    # num1 (int or float): first number
    # num2 (int or float): second number
    # num3 (int or float): third number
    # Returns:
    # (int or float): the maximum of the three numbers
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return num1
    
    return max(num1, max(num2, num3))

print(max_num(1, 2, 3))

# Example usage:
num1 = 20
num2 = 30
num3 = 40

print("Maximum number", max_num(num1, num2, num3))

