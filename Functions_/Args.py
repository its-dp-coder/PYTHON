#WAP that takes varible number of arguments and returns their sum.
def sum_all(*args):
   print(args)
   return sum(args)
print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5,5,6,7,7))