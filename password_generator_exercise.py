import random

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numeric_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ';', ':', "'", '"', '<', '>', ',', '.', '/', '?']

n_letters=int(input('How many letters do you want in your password?\n'))
n_nums=int(input('How many numbers do you want in your password?\n'))
n_char=int(input('How many special keyword do you want in your password?\n'))


password_list=[]

for a in range(1,n_letters+1):
    letters = random.choice(alphabet_list)
    password_list+=letters

for n in range(1,n_nums+1):
    nums=random.choice(numeric_list)
    password_list +=nums

for s in range(1,n_char+1):
    special = random.choice(special_characters)
    password_list+=special

random.shuffle(password_list)

passwd=''
for a in password_list:
    passwd+=a
print(f'This is Your Secure Password:\n{passwd}')

