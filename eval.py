import sys
sys.set_int_max_str_digits(10000000) # to enable you to use 10,000,000 ten million digits for each
e = input("Enter formula to evaluate f(x,y,z) =   ")
while True:
    x = float(input("x="))
    y = float(input("y="))
    z = float(input("z="))
    print(f'f({x},{y},{z}) = ',eval(e))
