stock_list = list(map(int, input().split(",")))
import sys

if len(stock_list) == 0:
    print(0)

    sys.exit()

max_fail = 0
diff = 0
dp = len(stock_list) * [0]
dp[0] = 0
for i in range(0, len(stock_list) - 1):
    if stock_list[i + 1] - stock_list[i] < 0:
        max_fail += stock_list[i + 1] - stock_list[i]
    # dp[i] = dp[i-1]+stock_list[i]-stock_list[i-1] if dp[i-1]+stock_list[i]-stock_list[i-1]<0 else 0

print((max_fail))