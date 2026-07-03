capital={'India':'New Delhi','USA':'Washington DC','UK':'London','France':'Paris'   }
for key,value in capital.items():
    print(key,value)

print(capital.get('India'))    

print(len(capital))

print(capital.keys())
print(capital.values())
print(capital.pop('UK'))

capital_copy=capital.copy()
print(capital_copy)
capital_copy['germeny']='berlin'
print(capital_copy)

