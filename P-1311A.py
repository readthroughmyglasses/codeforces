#Difficulty Range: 800
#Problem Code: 1311A
#Problem Link: https://codeforces.com/problemset/problem/1311/A
#Problem Name: Add Odd or Subtract Even


def oddeven(nums):
    if (nums[0]<nums[1] and sum(nums)%2==1)or (nums[0]>nums[1] and sum(nums)%2==0):
        return 1
    elif (nums[0]<nums[1] and sum(nums)%2==0)or (nums[0]>nums[1] and sum(nums)%2==1):
        return 2
    else:
        return 0
for i in range(int(input())):
    x =list(map(int,input().split()))
    print(oddeven(x))
