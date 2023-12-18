nums=[1,2,3,4,5,6,7,8,9,10]
squares=[]
for a in nums:
    if a==6:
        break
    sq=a **12
    squares.append(sq)
    print(squares)
else:
    print('for loop completed successfully')

