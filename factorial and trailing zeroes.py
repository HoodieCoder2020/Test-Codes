def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)


n = int (input())
print(factorial(n))
result = str(factorial(n))

result = result[::-1]

count = 0
for i in range(len(result)):
    if result[i] == "0":
        count+=1
    else :
        break

print("number of traling zeroes is " , count)