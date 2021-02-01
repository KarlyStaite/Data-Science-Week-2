def depreciation(inp_v,inp_d):
    v = inp_v
    d = inp_d
    y=0
    while v >= 1000:
        print("After year " + str(y) + " the value of the motorcycle is £" + "%0.2f" %(v))
        y = y + 1
        v = v - (v*d/100)

val = int(input("What is the intial value? "))
dep = int(input("What is the depriciation rate in %? "))

depreciation(val,dep)