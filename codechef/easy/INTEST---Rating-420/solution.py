# cook your dish here
# cook your dish here
T = int(input())
for _ in range(T):
    N = input().strip()
    
    # The first digit is at index 0, and the last digit is at the last index (-1)
    first_digit = int(N[0])
    last_digit = int(N[-1])
    
    print(first_digit + last_digit)
    
