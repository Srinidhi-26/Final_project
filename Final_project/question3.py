num = int(input("Enter a non-negative integer: "))

factorial = 1
if num < 0:
    print("Negative integer does not have factorial, Please Enter positive integer ")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for j in range(1, num + 1):
        factorial = factorial * j
    print("The factorial of", num, "is", factorial)


