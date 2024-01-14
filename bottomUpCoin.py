def coinChange(moedas, troco):
    dp = [troco+1] * (troco+1)           
    dp[0] = 0

    for i in range(1, troco+1):
        for j in moedas:
            if i >= j:
                dp[i] = min(dp[i], 1 + dp[i - j])    #moeda 4, troco 7 // dp[7] = 1 + dp[7-4]
    
    return dp[troco] if dp[troco] != (troco + 1) else -1



moedas = [1, 2, 4, 8]
troco = 7

print(coinChange(moedas, troco))