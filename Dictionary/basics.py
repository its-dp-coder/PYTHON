dict={'uttar pradesh':'lucknow','maharashtra':'mumbai','tamil nadu':'chennai','karnataka':'bangalore    '}
print(dict['uttar pradesh'])
for key in dict:
    print(key,dict[key], end='\n ')

dict['karnataka']='bangalore'
print(dict)