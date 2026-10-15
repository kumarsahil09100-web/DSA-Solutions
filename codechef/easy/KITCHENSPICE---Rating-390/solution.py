# cook your dish here
t =int(input())
for i in range(t):
    x = int(input())
    if(x<4):
        print("mild")
    elif(4<=x<7):
        print("medium")
    else:
        print("hot")
