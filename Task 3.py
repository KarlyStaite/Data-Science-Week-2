def calc(inp_x,inp_y,inp_o):
    x = inp_x
    y = inp_y
    o = inp_o

    if o == "a":
        print(x + y)
    elif o == "b":
        print(x - y)
    elif o == "c":
        print(x * y)
    elif o == "d":
        print(x / y)
    elif o == "e":
        print(x ** y)
    elif o == "f":
        print(x * x)
    elif o == "g":
        print(y * y)
    else:
        print("invalid opperator")


val1 = int(input("Enter the first value "))
val2 = int(input("Enter the seccond value "))

print("'a' for addition")
print("'b' for subtraction")
print("'c' for multiplication")
print("'d' for division")
print("'e' first value to the power of the seccond")
print("'f' for value 1 squared")
print("'g' for value 2 squared")
opp = input("Enter the operator ")

calc(val1,val2,opp)