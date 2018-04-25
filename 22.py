def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    string = ""
    open = 0
    close = 0
    array = []
    backtrack(string, open, close, array, n)
    return array

def backtrack(string, open, close, array, n):
    if len(string) == n*2:
        array.append(string)
        return

    if open < n:
        open += 1
        backtrack(string+"(", open, close, array, n)
        open -= 1
    if close < open:
        close += 1
        backtrack(string+")", open, close, array, n)
        close -= 1

print(generateParenthesis(2))
