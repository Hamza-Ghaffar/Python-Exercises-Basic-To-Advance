#small pizza =100
#Medium pizza =200
#Large pizza =300

#Pepporni for small = 30
#Pepporni for medium = 40
#Pepporni for large = 50

#extra cheez for any pizza =50

print(f'Welcome To Pizza House')

size_dict= dict(small = "small", medium = 'medium', large = "large")

print(f'{size_dict["small"]}\n{size_dict["medium"]}\n{size_dict["large"]}')

size=input(f' \nSelect Your Pizza Size: S/M/L \n')

oder_small=100
oder_medium=200
oder_large=300

pep_dict= dict(small = 30, medium = 40, large = 50)
chees=20 #for all sizes
amount=0

if size == 's' or size == 'S':
    amount+=oder_small
    print(f'Large Pizza Price: {oder_small}')
elif size == 'm' or size == 'M':
    amount += oder_medium
    print(f'Large Pizza Price: {oder_medium}')
else:
  size == 'l' or size == 'L'
  amount += oder_large
  print(f'Large Pizza Price: {oder_large}')


adon_pepperoni = input(f'Press [y/n]\nIf You want to add extra doping of pepperoni: \n')
if adon_pepperoni=="y" or adon_pepperoni=="Y":
    if size == 's' or size == 'S':
        amount += pep_dict["small"]
    elif size == 'm' or size == 'M':
        amount += pep_dict["medium"]
    else:
        amount+=pep_dict["large"]

adon_extrachees = input(f'Press [y/n]\nIf You want to add extra chees')
if adon_extrachees=="y" or adon_extrachees=="Y":
    if size == 's' or size == 'S':
        amount += 20
    elif size == 'm' or size == 'M':
        amount +=30
    else:
        amount += 40

print(f'Final{amount}')






