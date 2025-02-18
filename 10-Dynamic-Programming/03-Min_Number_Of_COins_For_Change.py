# Link: https://www.algoexpert.io/questions/Min%20Number%20Of%20Coins%20For%20Change


def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    numsOfCoins = [float("inf") for amount in range(n+1)]
    numsOfCoins[0]= 0

    for denom in denoms:
        for amount in range(len(numsOfCoins)):
            if denom <= amount:
                numsOfCoins[amount] = min(numsOfCoins[amount],numsOfCoins[amount-denom]+1)


    return numsOfCoins[n] if numsOfCoins[n] != float("inf") else  -1
                                         
