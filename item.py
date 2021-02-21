T =int(input())
arr =[  ]

for i in range(T):
    n = int(input())
    c =  input().split()
    c = [int(item) for item in c]
    arr.append(c)

a = []
b =[]
for i in range(len(arr)):
    for j in range(len(arr[i])-1):
        if j == 0:
            b.append(arr[i][0])
        else:
            b.append(arr[i] [j+1] - arr[i] [j]) #
            a.append(b)

for i in range(len(a)):
    for j in range(len(a[i])):
        c = [str(item) for item in a[i][j]]

        array = ' '.join(c)
        print(array)
