file = open('youtube.txt', 'w')
try:
    file.write('Hello')
finally:
    file.close()  

with open('youtube.txt', 'w')   as file:
    file.write('Hello alter way error handling')   
