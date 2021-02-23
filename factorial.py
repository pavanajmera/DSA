
def factorial():
    n = int(input("Enter number:"))
    result = 1
    for i in range(2,n+1):
        result = result * i
    print("\nFactorial of", n ," is: ", result,"\n")

factorial()