# Minimum Characters required to make a Words

def minimumCharactersForWords(words):
    # Write your code here.
    global_map = {}
    
    # Count characters in each word
    for word in words:
        temp_map = {}
        # Count frequency of characters in current word
        for char in word:
            temp_map[char] = temp_map.get(char, 0) + 1
            
        # Update global map with maximum frequency needed
        for char, count in temp_map.items():
            global_map[char] = max(global_map.get(char, 0), count)
    
    # Convert map to list of characters with repetition
    result = []
    for char, count in global_map.items():
        result.extend([char] * count)
        
    return result


# Test the minimumCharactersForWords function

print(minimumCharactersForWords(["this", "that", "did", "deed", "them!"])) #['t', 'h', 'i', 's', 'a', 'd', 't', 'e', 'm', '!']
print(minimumCharactersForWords(["this", "that", "did", "deed", "them"])) #['t', 'h', 'i', 's', 'a', 'd', 't', 'e', 'm']
