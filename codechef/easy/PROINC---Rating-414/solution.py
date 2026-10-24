# cook your dish here
t = int(input())
for i in range(t):
    x,y = map(int, input().split())
    c = x-y
    print(int (x+(x*10/100))-c)
    