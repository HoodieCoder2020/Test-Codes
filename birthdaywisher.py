import math 
l ,v1 , v2 = map(int , input().split())

for _ in range(int(input())):
  query = int(input())
  a =pow(query,0.5) * math.sqrt(2)/ (v1-v2)
  print(a)