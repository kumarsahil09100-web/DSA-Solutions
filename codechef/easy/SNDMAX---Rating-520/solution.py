# cook your dish here
# cook your dish here
t = int(input())
for i in range(t):
    nums = list(map(int, input().split()))
    nums.sort()
    print(nums[1])
