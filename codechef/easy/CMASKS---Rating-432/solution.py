# cook your dish here
t = int(input())
for i in range(t):
    x,y = map(int, input().split())
    if(100*x > 10*y):
        print("cloth")
    elif(100*x < 10*y):
        print("disposable")
    else:
        print("cloth")