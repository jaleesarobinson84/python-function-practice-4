# Write a Python function called rev_string() to reverse a string

def rev_string(string):
# Reverse a given string
#aruguments:
# input_string (string): string to be reversed

# Returns:
# str: The reverse string
    return string[::-1]

print(rev_string('hello'))
print(rev_string('howdy'))

# Example usage:
rev_string = 'hello'
print("Reverse string", rev_string(rev_string))