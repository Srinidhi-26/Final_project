while True:
    size = int(input("Enter a size for the hexagon: "))
    if size <= 0:
        print("Invalid : Size must be a positive integer")
    else:
        break


for i in range(2*size-1):
    if i < size:
        print(" "*(size-i-1) + "* "*(i+1))
    else:
        print(" "*(i-size+1) + "* "*(2*size-i-1))
