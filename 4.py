print("bmi index measurement")
weight=float(input("Please enter your weight in kilograms : "))
height=float(input("Please enter your height in meters : "))

bmi=weight/height**2

if bmi<18.5:
    print("under weight")
elif 18.5<bmi<24.9:
    print("normal")
elif 25<bmi<29.9:
    print("over wieght")
elif  30<bmi<34.9:
    print("obese")
elif  bmi>35 :   
    print("extremely obese")