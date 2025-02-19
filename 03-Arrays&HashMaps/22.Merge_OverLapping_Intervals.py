# Merge the OverLapping Intervals

# Given a collection of intervals, merge all overlapping intervals.

def mergeOverlappingIntervals(intervals):
    # Write your code here.
    sortedIntervals = sorted(intervals,key = lambda x: x[0])

    mergeIntervals = []
    currentInterval = sortedIntervals[0]
    mergeIntervals.append(currentInterval)

    for nextInterval in sortedIntervals:
        _, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval

        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1]= max(currentIntervalEnd,nextIntervalEnd)
        else:
            currentInterval = nextInterval
            mergeIntervals.append(currentInterval)
            
    return mergeIntervals
