# cook your dish here
t = int(input())
for i in range(t):
    x= int(input())
    if(x<3):
        print("light")
    elif (x>=7):
        print("heavy")
    else:
        print("moderate")