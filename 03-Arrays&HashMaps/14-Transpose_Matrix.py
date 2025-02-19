# Transpose Matrix

def transposeMatrix(matrix):
    # Write your code here.
    transposeMatrix = []

    for col in range(len(matrix[0])):
        newRow=[]
        for row in range(len(matrix)):
            newRow.append(matrix[row][col])
        transposeMatrix.append(newRow)
        
    return  transposeMatrix 
