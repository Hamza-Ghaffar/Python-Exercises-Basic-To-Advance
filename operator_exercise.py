# Simple Calculate bmi=weight/hight²

my_weight=int(input('Enter Your Current Weight In Kg:'))
my_height=float(input('Enter Your Current Height In Meters:'))

bmi=my_weight/my_height**2

print('My BMI: ',int(bmi))
