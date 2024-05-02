# Write a Python function called num_within() to check whether a number falls in a given range
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.

def num_within(num, start, end):
    if num >= start and num <= end:
        return True
    else:
        return False
    
return_value = num_within(10, 5, 15)

print(return_value)

# Example usage:

num = 10
start = 5
end = 15

return_value = num_within(num, start, end)

if num_within(num, start, end, start, end):
    print("Number is within range")
else:
    print("Number is not within range")
