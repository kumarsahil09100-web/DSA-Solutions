# cook your dish here
t = int(input())
for  i in range(t):
    x,y = map(int, input().split())
    if((2*y)<=x):
        print("yes")
    else:
        print("no")
