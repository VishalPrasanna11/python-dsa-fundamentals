def hasSingleCycle(array):
    # Write your code here.
    visited =0
    currentIdx = 0
    while visited < len(array):
        if visited > 0 and currentIdx == 0:
            return False

        visited += 1
        currentIdx = getNextIdx(currentIdx,array)

    return currentIdx == 0


def getNextIdx(currentIdx,array):
    jump = array[currentIdx]
    nextIdx = ( currentIdx + jump) % len(array)
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)
   