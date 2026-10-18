# cook your dish here

X, Y = input().split()
X = int(X)
Y = float(Y)
if X % 5 == 0 and Y >= X + 0.50:
    Y -= (X + 0.50)
print(f"{Y:.2f}")