# cook your dish here
t = int(input())
while t>0:
    n,x,y =map(int,input().split())
    if(n<= x*y):
        print("yes")
    else:
        print("no")
    t -=1