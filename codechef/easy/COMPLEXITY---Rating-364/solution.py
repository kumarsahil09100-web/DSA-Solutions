# cook your dish here
t = int(input())
while(t>0):
    x,y = map(int,input().split())
    if(x>y):
        print("yes")
    else:
        print("no")
    t -=1