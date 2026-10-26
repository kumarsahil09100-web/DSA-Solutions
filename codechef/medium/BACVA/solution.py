# cook your dish here
t = int(input())

for _ in range(t):
  
    a = list(map(int, input().split()))

    s = 0
    for i in range(n):
        s += a[i]

    print(s)