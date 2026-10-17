# cook your dish here

t =  int(input())
for i in range(t):
    x,y = map(int, input().split())
    if(x>y):
        print("second")
    elif(y>x):
        print("first")
    else:
        print("any")