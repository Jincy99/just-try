#calculator
one=0.0;two=0.0
try:
    one=float(input("First data: "))
    two=float(input("second data: "))
except ValueError as verror:
    print(verror,"\n Enter only numeric data: ")
    one=float(input("First data: "))
    two=float(input("second data: "))
finally:
    option=input("Operation to do: ")
    if option=="+":
        print(one+two)
    elif option=="-":
        print(one-two)
    elif option=="*":
        print(one*two)
    elif option=="/":
        print(one/two)
    print("Calculation done")
