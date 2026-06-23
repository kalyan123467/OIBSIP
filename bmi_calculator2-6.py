# BMI Formula: BMI = Weight (kg) / (Height (m) ** 2)

print("=" * 50)
print("         ADVANCED BMI CALCULATOR")
print("=" * 50)

# User Information
name = input("Enter your name: ")

try:
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    # Input Validation
    if age <= 0:
        print("Age must be greater than 0.")
    elif weight <= 0:
        print("Weight must be greater than 0.")
    elif height <= 0:
        print("Height must be greater than 0.")
    else:
        # BMI Calculation
        bmi = weight / (height ** 2)

        print("\n" + "=" * 50)
        print("BMI REPORT")
        print("=" * 50)

        print("Name   :", name)
        print("Age    :", age)
        print("Weight :", weight, "kg")
        print("Height :", height, "m")
        print("BMI    :", round(bmi, 2))

        # BMI Classification
        if bmi < 18.5:
            category = "Underweight"
            advice = "Increase calorie intake and follow a healthy diet."

        elif bmi < 25:
            category = "Normal Weight"
            advice = "Maintain your current healthy lifestyle."

        elif bmi < 30:
            category = "Overweight"
            advice = "Exercise regularly and eat balanced meals."

        else:
            category = "Obese"
            advice = "Consult a healthcare professional."

        print("Category :", category)

        print("\nHealth Advice:")
        print(advice)

        print("\nBMI Classification Table")
        print("-" * 30)
        print("Below 18.5      : Underweight")
        print("18.5 - 24.9     : Normal Weight")
        print("25.0 - 29.9     : Overweight")
        print("30.0 and Above  : Obese")

        print("\nHealth Tips")
        print("- Drink enough water")
        print("- Exercise regularly")
        print("- Eat nutritious food")
        print("- Sleep 7-8 hours daily")

except ValueError:
    print("Invalid input! Please enter numeric values.")

print("\n" + "=" * 50)
print("Thank you for using BMI Calculator")
print("=" * 50)
