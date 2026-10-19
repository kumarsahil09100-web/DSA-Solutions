# cook your dish here
t =int(input())
for i in range(t):
    n,x = map(int, input().split())
    if(x>=n/2):
        print("yes")
    else:
        print("no")
