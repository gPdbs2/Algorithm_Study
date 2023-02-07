import sys
input = sys.stdin.readline

n = int(input())
dp = [1, 3] + [0]*(n+1)

for i in range(2, n+1):
    dp[i] = (dp[i-2] + dp[i-1]*2)%9901
print(dp[n])

# 걸린 시간 : 약 87분