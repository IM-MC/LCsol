def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """

    if len(digits) == 0:
        return []

    dict = {
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyz"
    }

    arr = []
    curr = ""
    index = 0

    def backtrack(array, curr, digits, index):

        if len(curr) == len(digits):
            array.append(curr)
            return

        for char in dict[digits[index]]:
            backtrack(array, curr + char, digits, index + 1)

    backtrack(arr, curr, digits, index)

    return arr

print(letterCombinations("233"))
