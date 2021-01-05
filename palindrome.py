# Find Given number is palindrome or not
def palindrome(n):
    reverse = 0
    temp = n  
    while(temp > 0):
        a = temp % 10
        reverse = reverse * 10 + a
        temp = temp // 10
    return reverse == n

n = 123
print(palindrome(n))
