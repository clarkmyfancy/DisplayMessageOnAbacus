def showAbacus(number):
    reversedNumber = (str(number)[len(str(number))::-1])
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

def convertPhrase(word):
    phrase = word.lower()
    # assig each letter (including space) a prime number. The more prevelent the letter in words, the lower the prime number. In this implementation, I rearranged some of the values to make the specific message I wanted to encode fit in a number less than ~10e12.
    letters = {
        ' ': 2,
        'e': 3,
        't': 5,
        'a': 7,
        'w': 11,
        'c': 13,
        'n': 19,
        's': 23,
        'k': 29,
        'h': 31,
        'd': 37,
        'l': 41,
        'u': 43,
        'i': 47,
        'm': 53,
        'f': 59,
        'y': 61,
        'o': 67,
        'g': 71,
        'p': 73,
        'b': 79,
        'v': 83, 
        'r': 89,
        'x': 97,
        'q': 101,
        'j': 103,
        'z': 107
    }
    multiplicativeIdenity = 1
    result = multiplicativeIdenity
    
    for character in phrase:
        characterValue = letters[character]
        result *= characterValue
    return result

if __name__ == '__main__':
    phrase = input("What phrase would you like to convert? ")
    numberRepresentation = convertPhrase(phrase)
    print()
    print("Public Key Below")
    showAbacus(numberRepresentation)
