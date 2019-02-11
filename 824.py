def toGoatLatin(S):
    """
    :type S: str
    :rtype: str
    """

    res = ""

    wordList = S.split()
    spaces = len(wordList) - 1

    vowels = {'a','e','i','o','u','A','E','I','O','U'}
    current = "a"

    for word in wordList:

        if word[0] not in vowels:
            word = word[1:] + word[0]

        word += "ma" + current
        current += "a"

        temp = str(word)

        res += temp

        if spaces > 0:
            res += " "
            spaces -= 1

    return res

print(toGoatLatin("I speak Goat Latin Everyday"))
print(toGoatLatin(""))
