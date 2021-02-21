# checking armstrong number
n = input()
sumofnumber = sum([int(item)**len(n)  for item in n])
if sumofnumber ==int(n):
    print("Armstrong number")
else:
    print("Not armstrong number")    
