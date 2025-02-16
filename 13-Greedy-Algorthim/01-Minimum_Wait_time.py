# Minimum Wait Time

# You're given a non-empty array of positive integers representing the amounts of time that specific queries take to execute. Only one query can be executed at a time, but the queries can be executed in any

# order.

# A query's wait time is defined as the amount of time that it must wait before its execution starts. In other words, if a query is executed second, then its wait time is the duration of the first query; if a query is executed

def minimumWaitingTime(queries):
    # Write your code here.

    queries.sort()
    totalWaitTime = 0

    for idx, duration in enumerate(queries):
        queries_left = len(queries)-(idx+1)
        totalWaitTime += duration*queries_left

    return totalWaitTime

# Test the function

queries = [3, 2, 1, 2, 6]

print(minimumWaitingTime(queries)) # 17

queries = [2, 1, 1, 1]

print(minimumWaitingTime(queries)) # 6