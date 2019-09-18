def showAbacus(number):
    reversedNumber = str(number)[len(str(number))::-1]
    abacusLine = ""
    for i, value in enumerate(reversedNumber): 
        digit = int(value)
        if (digit == 0):
            abacusLine = 'oo | ooooo'
        elif (digit == 1):
            abacusLine = 'oo |o oooo'
        elif (digit == 2):
            abacusLine = 'oo |oo ooo'
        elif (digit == 3):
            abacusLine = 'oo |ooo oo'
        elif (digit == 4):
            abacusLine = 'oo |oooo o'
        elif (digit == 5):
            abacusLine = 'o o| ooooo'
        elif (digit == 6):
            abacusLine = 'o o|o oooo'
        elif (digit == 7):
            abacusLine = 'o o|oo ooo'
        elif (digit == 8):
            abacusLine = 'o o|ooo oo'
        elif (digit == 9):
            abacusLine = 'o o|oooo o'
        print('----------')
        print(abacusLine)
    print('---------')
    return

def main():
    letters = {
        ' ': 2,
        'e': 3,
        't': 5,
        'a': 7,
        'o': 11,
        'i': 13,
        'n': 19,
        's': 23,
        'r': 29,
        'h': 31,
        'd': 37,
        'l': 41,
        'u': 43,
        'c': 47,
        'm': 53,
        'f': 59,
        'y': 61,
        'w': 67,
        'g': 71,
        'p': 73,
        'b': 79,
        'v': 83, 
        'k': 89,
        'x': 97,
        'q': 101,
        'j': 103,
        'z': 107
    }
    phrase = "pat with a t"
    result = 1
    for character in phrase:
        characterValue = letters[character]
        result *= characterValue
    return result

if __name__ == '__main__':
    result = main()
    print(showAbacus(result))


