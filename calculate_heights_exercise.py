height = input('Enter Heights')
heights=height.split()
print(heights)

count=0
for h in heights:
    count =count+1
print(count)

for i in range(count):
    heights[i]=float(heights[i])
print(heights)

sum=0
for s in heights:
    sum+=s
print(sum)
av=sum/count
print(av)

