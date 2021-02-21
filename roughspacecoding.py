T = int(input())
arr = []
if T == 1:
    for i in range(T):
        n = int(input())
        c = input().split()
        c = [int(item) for item in c]
        c.sort()
        arr.append(c)

    a = [list[0] for list in arr]
    for list in arr:
        for i in range(len(list)-1):
            a.append(list[i+1] - list[i])

    

    final = [str(item) for item in a]
    ans = " ".join(final)
    print(ans)


else:
        for i in range(T):
            n = int(input())
            c = input().split()
            c = [int(item) for item in c]
            c.sort()
            arr.append(c)
        
        
        for list in arr:
            a = [list[0]]
            for i in range(len(list)-1):
                a.append(list[i+1] - list[i])
            final = [str(item) for item in a]
            ans = " ".join(final)
            print(ans)
            a.clear()
        

    
        
