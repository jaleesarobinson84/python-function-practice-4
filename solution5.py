# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print

def pascal(n):
    print(" " * (n-1), end="")
    num = 1
    for i in range(n):
        for j in range(i+1):
            print(num, end=" ")
            if j == 0 or j == i:
                print(1, end=" ")

                num = num * (i - j) // (j + 1)
                print(num, end=" ")
                print()

pascal(10)





