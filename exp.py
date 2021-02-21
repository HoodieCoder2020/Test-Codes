a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = list(zip(a, b))
print(x)


x1,y1 = zip(*x) 
print(list(x1))
print(list(y1))
print(y1)

#use the tuple() function to display a readable version of the result:

