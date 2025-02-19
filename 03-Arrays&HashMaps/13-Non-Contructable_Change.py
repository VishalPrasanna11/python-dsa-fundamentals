# Non Contructable Change

# You're given an array of positive integers representing the values of coins in your possession. Write a function that returns the minimum amount of change (the minimum sum of money) that you cannot create. The given coins can have any positive integer value and aren't necessarily unique (i.e., you can have multiple coins of the same value).

def nonConstructibleChange(coins):
    # Write your code here.
    notPossible = 0
    coins.sort()

    for coin in coins:
        if coin > notPossible + 1:
            return  notPossible + 1

        notPossible += coin
    return notPossible+1
