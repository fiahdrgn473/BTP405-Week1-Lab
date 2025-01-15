
def getFibonacci(param):
    i = 1
    print ("[", end="")
    x = 1
    y = 0
    while i < param:
        print (y, end="")
        print (", ", end="")
        z = x + y
        y = x
        x = z
        i = i + 1
    if i == param:
        print (y, end="")
    print("]", end="")

getFibonacci(10)
