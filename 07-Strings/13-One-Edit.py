def oneEdit(stringOne, stringTwo):
    n = len(stringOne)
    m = len(stringTwo)

    if abs(n-m)>1:
        return False

    for i in range(min(n,m)):
        if stringOne[i]!=stringTwo[i]:
            if n>m:
                return stringOne[i+1:]== stringTwo[i:]
            elif m>n:
                  return stringOne[i:]== stringTwo[i+1:]
            else:
                  return stringOne[i+1:]== stringTwo[i+1:]

    return True

# Test the oneEdit function
print(oneEdit("abc","ab")) #True
print(oneEdit("abc","abc")) #True

print(oneEdit("abc","abcd")) #True
print(oneEdit("abc","abdc")) #True
print(oneEdit("ac","abcc")) #True
print(oneEdit("abc","ab")) #True
