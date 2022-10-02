def reverseNumber(x):
    if (x < 0):
        isNegative = True
    else:
        isNegative = False
    xCopy = abs(x)
    digits = []
    while (xCopy >= 0):
        digits.append(xCopy % 10)
        xCopy = xCopy // 10
    for i in range (0, len(digits)//2):
        temp = digits[i]
        digits[i] = digits[-i-1]
        digits[-i-1] = temp
    
    x = 0
    multiplier = 10
    for i in range(len(digits)-1, -1, -1):
        x = x + (digits[i] * multiplier)
        multiplier = multiplier * 10
    
    if (isNegative):
        x = x * -1
    
    if (x < (2 ** 31) or (x > ((2 ** 31) - 1))):
        x = 0
    
    return x