# cook your dish here
t = int(input())
for i in range(t):
    a, b, c = map(int,input().split())
    if(a>b and a>c):
        print("alice")
    elif(b>a and b>c):
        print("bob")
    else:
        print("charlie")