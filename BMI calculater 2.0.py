weight=int(input("enter your weight in kg="))
height=float(input("enter your height in m="))
BMI=weight/(height**2)
print(f"your bmi={BMI}")
if(BMI<=18.5):
    print("you are undr")
elif(BMI>18.5 and BMI<=24.9):
    print("you are healthy weight")
elif(BMI>24.9 and BMI<=29.9):
    print("you are over weight")
else:
    print("you have obesity")