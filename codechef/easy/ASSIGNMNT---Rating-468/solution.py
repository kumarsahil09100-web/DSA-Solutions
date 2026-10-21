# cook your dish here
t = int(input())
for  i in range(t):
    x,y,z = map(int,input().split())
    if(((x*y)/60)<=24*z):
        print("yes")
    else:
        print("no")
