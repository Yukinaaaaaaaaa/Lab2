def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = (weight / (height * height))
    print("BMI = " + str(bmi))
    if (bmi < 18.5):
        print("underweight")
    elif(18.5 <= bmi and bmi <= 25):
        print ("Normal Weight")
    else:
        print ("OverWeight")

# Corrected values: using numeric values instead of strings
calculate_bmi(weight=57, height=1.73)