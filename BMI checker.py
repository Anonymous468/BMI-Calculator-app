#BMI calculator

def BMI(weight,height):
    bmi=weight/(height*height)
    print("BMI=",bmi,"\nresult:\n")
    if bmi<=18.4:
        print("UNDERWEIGHT")
    elif bmi>=18.5 and bmi<=24.9:
        print("NORMAL WEIGHT")
    elif bmi>=25.0 and bmi<=29.9:
        print("PRE-OBESITY")
    elif bmi>=30.0 and bmi<=34.9:
        print("OBESITY CLASS 1")
    elif bmi>=35.0 and bmi<=39.9:
        print("OBESITY CLASS 2")
    else:
        print("OBESITY CLASS 3")

        
print("""BMI calculator for Adult Age 20+

NOTE:- BMI varies with age and may not be accurate always...

ALWAYS CONSULT A GOOD DOCTOR\n\n\n""")


weight=float(input("Enter weight in kg:\t"))

print("""Choose the unit of height:

1)ft inches
2)centimetres
3)metres\n""")

choice=int(input("Enter your choice:\t"))
print("\n")

if choice==1:
    feet=int(input("Enter the foot part:\t"))
    inch=int(input("Enter inches part\n(NOTE:- If there is no inch part, put input as 0):\t"))
    inch_to_feet=0.0833333*inch
    height_in_feet=feet+inch_to_feet
    height_m=0.305*height_in_feet
    BMI(weight,height_m)
             
elif choice==2:
    height=float(input("Enter height in cm:\t"))
    height_m=height/100
    BMI(weight,height_m)
    
elif choice==3:
    height=float(input("Enter height in metres"))
    BMI(weight,height)
    
else:
    print("ERROR: WRONG INPUT")
