#def decode_message( s: str, p: str) -> bool:

# write your code here


def decode_message(message, pattern):
    # Use a dynamic programming approach to solve the pattern matching problem
    m, n = len(message), len(pattern)
    
    # dp[i][j] will be True if pattern[0..j-1] matches message[0..i-1]
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    # Handle the case where pattern starts with '*'
    for j in range(1, n + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif pattern[j - 1] == '?' or pattern[j - 1] == message[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]

    return dp[m][n]

