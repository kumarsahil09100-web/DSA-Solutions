# cook your dish here
t = int(input())
for i in range(t):
    x,y = map(int, input().split())
    if((x!=0 or y != 0) and x ==y):
        print("yes")
    else:
        print("no")