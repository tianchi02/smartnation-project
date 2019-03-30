height=float(input("Enter your height: "))
weight=float(input("Enter your weight: "))
BMI= height * 2 + weight
print（BMI）
if BMI < 18.5:
 print("underweight,eat more meat and protein-rich food XD.")
elif 18.5 < BMI < 25:
 print("normal,keep up with the good habits.")
elif 25 < BMI < 30:
 print("overweight,exercise more often.)
else:
 print（“obesity，please eat more vegetables and exercise regularly.")
