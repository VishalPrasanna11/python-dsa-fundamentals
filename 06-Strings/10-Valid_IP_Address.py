# Valid Ip Address
def validIPAddresses(string):
    ip_list = []
    
    def isValidOctet(octet):
        # Check if octet is empty or longer than 3 digits
        if not octet or len(octet) > 3:
            return False
        # Check for leading zeros
        if len(octet) > 1 and octet[0] == '0':
            return False
        # Check if number is between 0 and 255
        try:
            num = int(octet)
            return 0 <= num <= 255
        except ValueError:
            return False
    
    # Optimization: only process strings of valid length
    if len(string) < 4 or len(string) > 12:
        return []
        
    for i in range(1, min(4, len(string)-2)):
        for j in range(i+1, min(i+4, len(string)-1)):
            for k in range(j+1, min(j+4, len(string))):
                # Get all four octets
                first = string[0:i]
                second = string[i:j]
                third = string[j:k]
                fourth = string[k:]
                
                # Check if all octets are valid
                if (isValidOctet(first) and 
                    isValidOctet(second) and 
                    isValidOctet(third) and 
                    isValidOctet(fourth)):
                    
                    ip_list.append(f"{first}.{second}.{third}.{fourth}")
    
    return ip_list

# Time Complexity: O(n ^ 3)

# Test the validIPAddresses function

print(validIPAddresses("1921680"))
print(validIPAddresses("19216800"))
print(validIPAddresses("192168000"))
# print(validIPAddresses("1921680000"))
# print(validIPAddresses("19216800000"))
