# Iterative method:
def Count_Digits(n):
    count = 0
    while (n != 0):
        n = n // 10
        count = count + 1
    return count

n = 1
print('Number of digits in number is:',Count_Digits(n),'\n')

# Recursive method:

def count_digit(n):
    if (n == 0):
        return 0
    return 1 + count_digit(n // 10)

print("No of Digits in a number: ", count_digit(123),'\n')
