# PYTHON CALCULATOR

def box(text):
    
    padding = 65
    width = len(text) + padding * 2

    print("*" * (width+2))
    print("*" + " " * padding + text +" "*padding + "*")
    print("*"* (width+2))


box("OFF")

ac = input("Enter ON: ").lower()

if ac == "on":
    box("ON")

    num1 = float(input("Enter 1st value: "))
    oper = input("Enter Arthematic Operation: ").strip().lower()
    num2 = float(input("Enter 2st value: "))

    if oper in ["+","add","sum"]:
        ans = num1 + num2
        print(f"Sum of given values is: {round(ans,2)}")

    elif oper in ["-","subtraction"]:
        ans = num1 - num2
        print(f"Subraction of given values is: {round(ans,2)}")

    elif oper in ["*","multiply" ,"multipl","product"]:
        ans = num1* num2
        print(f"Product of given values is: {round(ans,2)}")

    elif oper in ["/","devide"]:
        ans = num1 / num2
        print(f"Devide of given Values is: {round(ans,2)}")
    else:
        print(f"The given '{oper}' is Wrong Operation.")

else:
    box("OFF")
    
        

