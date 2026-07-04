#Sum of Even Numbers
number=[1,2,3,4,5,6,7,8,8,9,10]
sum=0
for i in number:
    if i%2==0:
        sum+=i
print("The sum of even numbers in the list is:",sum)    