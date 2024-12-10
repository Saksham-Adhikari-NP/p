Opertor = input("enter an operator + - * /")
N1 = float(input("enter the 1st number"))
N2 = float(input("Enter the 2nd number"))
if Opertor == "+":
    R = N1 + N2
    print(f"the result is {R}")
elif Opertor == "-":
    R = N1 - N2
    print(f"the result is {R}")
elif Opertor == "*":
    R = N1 * N2
    print(f"the result is {R}")
elif Opertor == "/":
    R = N1 / N2
    print(f"the result is {R}")
else :
    print ( "operator is not valid")
    