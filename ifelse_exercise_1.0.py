my_weight=int(input('Enter Your Current Weight In Kg:'))
my_height=float(input('Enter Your Current Height In Meters:'))

bmi=my_weight/my_height**2
if bmi <18.5:
    print(f'My BMI:{int(bmi)} and you are underweight ', )
elif bmi < 25:
    print(f'My BMI:{int(bmi)} and you have a normal weight ', )
elif bmi < 30:
    print(f'My BMI:{int(bmi)} and you have a overweight', )
elif bmi < 35:
    print(f'My BMI:{int(bmi)} and you have a Obese', )
else:
    print(f'My BMI:{int(bmi)} and you have a clinically Obese', )