print("WELCOME TO THE BMI CALCULATOR")
def calculate_bmi():
    while True:
        try:
            weight=float(input("Enter your weight (kg): "))
            height=float(input("Enter your hight (m): "))
            if weight<=0 or height<=0:
                print("weight and height must be greater than zero.") 
            else:
                break
        except ValueError:
            print("Inavlid input! please enter numeric values only.")
            continue
       
    bmi=weight/(height**2)
    bmi=round(bmi,2)
    print(f"Your BMI is: {bmi}")
    return bmi

def bmi_category(bmi):
        print("BMI category:")
        if bmi<18.5:
            print("Underweight")
        elif bmi>=18.5 and bmi<=24.9:
            print("Normal")
        elif bmi>=25 and bmi<=29.9:
            print("Overweight")
        elif bmi>=30:
            print("Obese")
        else:
            print("Invalid input")
def another_bmi():
    while True:
        another=input("Would you like to calculate another BMI? (yes/no): ").strip().lower()
        if another=="yes":
         bmi=calculate_bmi()
         bmi_category(bmi)
        elif another=="no":
         print("Thank you for using the BMI Calculator")
         print("Have a great day!")
         exit()
        else: 
          print("Please enter yes/no")  
bmi=calculate_bmi()
bmi_category(bmi)
another_bmi()
