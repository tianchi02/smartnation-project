height=float(input("Enter your height: "))
weight=float(input("Enter your weight: "))
BMI= height * 2 + weight
print（BMI）
if BMI < 18.5:
 print("underweight,eat more meat and protein-rich food XD.")
 print("Exercises recommended:5km run every week and 5 sets of push ups every day.")
elif 18.5 < BMI < 25:
 print("normal,keep up with the good habits.")
 print("Exercises recommended:10km run every week and 10 sets of push up everyday.")
elif 25 < BMI < 30:
 print("overweight,exercise more often.)
 print（”Exercises recommended：15km run every week and climbing mountains once a week.")
else:
 print（“obesity，please eat more vegetables and exercise regularly.")
 print("Exercises recommended:15km run every week and climbing mountains twice a week.")

