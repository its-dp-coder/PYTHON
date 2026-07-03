num=[1,2,3,4,5,6,7,8,9,10]
print(num[0:5])
print(num[5:10])
print(num[0:10:2])

# Replace value

num[3]=100
print(num)

city=['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(city[0:3])
print(city[2:5])    
city[1:2]=['San Francisco']
print(city)
city[2:4]=['Seattle', 'Denver']
print(city)