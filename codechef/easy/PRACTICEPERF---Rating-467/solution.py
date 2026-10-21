# cook your dish here
p1, p2, p3, p4 = map(int, input().split())
s = 0

# Store the weeks in a list to iterate through their values
weeks = [p1, p2, p3, p4]

for pi in weeks:
    # Check if he solved at least 10 problems
    if pi >= 10:
        s += 1

print(s)
      


    
