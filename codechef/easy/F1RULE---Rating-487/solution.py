# cook your dish here
# cook your dish here
t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    if 100 * y <= 107 * x:
        print("YES")
    else:
        print("NO")

