list1 = ["adarsh" , 'anand']
list2 = [1,2]

zipped =list(zip (list1 , list2))
print(zipped)
a , b = zip(*zip(list1 ,list2))
print(type(a) , list(a))
print(b)


a , b = zip(*zipped)

print(a)
print(b)