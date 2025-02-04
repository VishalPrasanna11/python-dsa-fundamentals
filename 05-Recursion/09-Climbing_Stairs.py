# Climbing Stairs


def climb_Stairs(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else : 
        return climb_Stairs(n-2)+climb_Stairs(n-1)
    
    
print(climb_Stairs(5))