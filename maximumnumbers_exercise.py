numbers = input('Enter Numbers')
number_list=numbers.split()
print(number_list)

count=0
for h in number_list:
    count =count+1


for i in range(count):
    number_list[i]=float(number_list[i])
print(number_list)

maimum_num=number_list[0]#99
for num in number_list:
    if num> maimum_num:
        maimum_num=num#now maxmum no is num
print(f'Maximum Number{maimum_num}')

