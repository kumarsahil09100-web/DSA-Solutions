# cook your dish here
t = int(input())
for i in range(t):
    x = int(input())
    if(x<=3):
        print("bronze")
    elif(3<x<=6):
        print("silver")
    else:
        print("gold")
