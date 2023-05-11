def multiplesbytwo(num0, num1):
    value=0
    for i in range(int(num1)):
        value=value+num0
    return value

def exponent(num0, num1):
    value=1
    for i in range (int(num1)):
        value=value*num0
    return value

def square(yer):
    return multiplesbytwo(yer, yer)

num0=4
num1=7
print(multiplesbytwo(num0, num1))
print(exponent(num0, num1))
print(square(num0))