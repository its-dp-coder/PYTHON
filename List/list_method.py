sports=['cricket', 'football', 'hockey', 'tennis', 'badminton   ']
sports.append('basketball')
print(sports)
sports.insert(2,'volleyball')
print(sports)
sports.remove('tennis')
print(sports)
sports_copy=sports.copy()
print(sports_copy)
sports_copy.append('table tennis')
print(sports_copy)

sqrd_num=[x**2 for x in range(1,11)]
print(sqrd_num)