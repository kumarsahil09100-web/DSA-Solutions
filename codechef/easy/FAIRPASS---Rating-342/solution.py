# cook your dish here
t = int(input())
while (t>0) :
    n,k = map(int, input().split())
    if(n>=k):
        print("no")
    else:
        print("yes")
    
    t -=1
   
