# cook your dish here
t = int(input())
for i in range(t):
    x,y,z = map(int, input().split())
    if(y+x <=z):
        print('2')
    elif x <= z:
        print('1')
    else:
        print('0')
            
   
    

