import math
print("welcome to my calculator")
print("please enter your choice")
print("jam:+")
print("tafrigh:-")
print("zarb:*")
print("taghsim:/")
print("radical:sqrt")
print("sin:sin")
print("cos:cos")
print("cot:cot")
print("tan:tan")
print("facrtorial:factorial")
op =input()
if op == "sin" or op == "cos" or op == "tan" or op == "cot" or op == "sqrt" or op == "factorial":
    a =float(input("please enter one number"))
    if op == "cos":
        r=a*math.pi/180
        c=math.cos(r)

    elif op == "sin":
        r=a*math.pi/180
        c=math.sin(r)

    elif op == "tan":
        r=a*math.pi/180
        c=math.tan(r)

    elif op == "cot":
        r=a*math.pi/180
        c=math.cot(r)

    elif op == "sqrt":
        c=math.sqrt(a)

    elif op == "factorial":
         a = int(input())
         c=math.factorial(a)

if op == "+" or op == "-" or op == "*" or op == "/":
    a =float(input("please enter one number"))
    b =float(input("please enter second number"))

    if op == "+":
          c=a+b
    elif op == "-":
          c=a-b
    elif op == "*":
          c=a*b
    elif op == "/":
          c=a/b
    
print(c)