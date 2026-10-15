# cook your dish here
t = int(input())
for i in range(t):
    x,y = map(int, input().split())
    if((x*3)>y):
        print("No")
    else:
        print("yes")
