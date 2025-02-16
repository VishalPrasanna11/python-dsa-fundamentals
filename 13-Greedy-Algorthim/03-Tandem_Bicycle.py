# Tandem Bicycle

# Problem Statement

# A tandem bicycle is a bicycle that's operated by two people: person A and person B. Both people pedal the bicycle, but the person that pedals faster dictates the speed of the bicycle. So if person A pedals at a speed of 5, and person B pedals at a speed of 4, the tandem bicycle moves at a speed of 5 (i.e., tandemSpeed = max(speedA, speedB)).

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
  
    if not fastest:
        redShirtSpeeds.sort()
    else :
        redShirtSpeeds.sort(reverse = True)

    blueShirtSpeeds.sort()
    total = 0
    for i in range(len(redShirtSpeeds)):
        rider1 = redShirtSpeeds[i]
        rider2 = blueShirtSpeeds[i]
        total  = total+ max(rider1,rider2)

    return total

# Test the function

redShirtSpeeds = [5, 5, 3, 9, 2]
blueShirtSpeeds = [3, 6, 7, 2, 1]
fastest = True

print(tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)) # 32