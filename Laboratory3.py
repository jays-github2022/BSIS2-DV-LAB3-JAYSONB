print("Hello! Please enter your name:")

name = input()

print("Enter your age:")

age = int(input())

print("Enter your weight (in kg):")

weight = int(input())

print("Enter your height (in cm):")

height = int(input())

print("These are your inputs:")

print(name)

print(age)

print(weight)

print(height)

bmiCompute = (weight/(height/100) * (height/100))

if (bmiCompute < 18.5):

  print("BMI Diagnosis: Underweight")

elif (bmiCompute < 24.9):

  print("BMI Diagnosis: Normal/Healthy")

elif (bmiCompute < 29.9):

  print("BMI Diagnosis: Overweight")

elif (bmiCompute > 30):

  print("BMI Diagnosis: Obese")
