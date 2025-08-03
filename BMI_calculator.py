def bmi(a,b):
    print(f"BMI: {a/(b*b)}")
    return a/(b*b)
def height_km(a):
    a*0.3048
    return a*0.3048
weight=float(input("Enter weight in kilograms_"))
height=float(input("Enter your height in meters:\n(For height in feets, enter '0'.\n"))
if height==0:
    height_feet=float(input("Enter your height in feet:"))
    height_meters=height_km(height_feet)
    result=bmi(weight,height_meters)
elif height>0:
    result=bmi(weight,height)
level1=18.5
level2=24.9
level3=29.9
if result<level1:
    print("You are 'Underweight'.")
elif result>=level1 and result<=level2:
    print("You have 'Healthy Weight'.")
elif result>level2 and result<=level3:
    print("You are 'Overweight'")
elif result>level3:
    print("You are suffering from 'Obesity'")
