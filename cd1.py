# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a,b,c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

#Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(lst):
    result = 1
    for i in lst:
        result *= i
    return result
# Write a Python function called rev_string() to reverse a string.
def rev_string(str):
    return str[::-1]


# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(num, start, end):
    return num >= start and num <= end



# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
def pascal(n):
    if n <= 0:
        return
    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # First element of each row is 1
        # Calculate middle elements of the row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Last element of each row is 1
        triangle.append(row)

    # Print each row
    for row in triangle:
        print(' '.join(map(str, row)))





# result
if __name__ == "__main__":
    print(max_num(1,2,3))
    print("_"*20)
    print(mult_list([1,2,3,4]))
    print("_"*20)
    print(rev_string("hello"))
    print("_"*20)
    print(num_within(3,2,4))
    print(num_within(3,1,3))
    print(num_within(10,2,5))
    print("_"*20)
    print(pascal(5))
    print("_"*20)
