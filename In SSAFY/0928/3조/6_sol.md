2번

```python
def fibo(n):
    dp = [0] * n
    for i in range(n):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]
```

시간복잡도: O(n)
