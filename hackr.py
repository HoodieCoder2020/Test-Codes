for i in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    a = min(array)
    left = array[:array.index(a)]
    right = array[array.index(a)+1 :]
    if left == sorted(left ,reverse=True) and right==sorted(right):
        print("Yes")
    else:
        print("No")