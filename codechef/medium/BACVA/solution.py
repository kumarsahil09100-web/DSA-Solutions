# cook your dish here
t = int(input())

for i in range(t):
    a = input()
    s = 0

    for j in a:
        s += int(j)

    if s % 10 == 0:
        print("Valid")
    else:
        print("Invalid")