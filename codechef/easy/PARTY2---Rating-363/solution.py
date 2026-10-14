# cook your dish here
t = int(input())
for i in range(t):
    n,x,k  = map(int, input().split())
    if((x*n)>k):
        print("no")
    else:
        print("yes")
    

