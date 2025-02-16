#Color Photos
# There even class students, have equal number of red and blue color dresses. The teacher wants to take a photo of the students. The students are standing in a row. The teacher wants to take a photo of the students in such a way that no two students with the same color dress are standing together. The teacher wants to know the number of ways in which the students can be arranged. The answer can be very large, so the teacher wants to know the answer modulo 10^9+7.

# Write a function that takes an integer n, the number of students, and returns the number of ways in which the students can be arranged.

def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort(reverse = True)
    blueShirtHeights.sort(reverse = True)

    shirtColorInFirstRow = "RED" if redShirtHeights[0]<blueShirtHeights[0] else "BLUE"

    for idx in range(len(redShirtHeights)):
        redShirtHeight =  redShirtHeights[idx]
        blueShirtHeight = blueShirtHeights[idx]

        if shirtColorInFirstRow =="RED":
            if redShirtHeight>=blueShirtHeight:
                return False
        else :
            if  blueShirtHeight>=redShirtHeight:
                return False

    return True

# Test the function

redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights = [6, 9, 2, 4, 5]

print(classPhotos(redShirtHeights, blueShirtHeights)) # True
print(classPhotos([5, 8, 1, 3, 4], [6, 9, 2, 4, 5])) # True