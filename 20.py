def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    brackets = []

    for char in s:
        if char == "(":
            brackets.append(")")
        elif char == "{":
            brackets.append("}")
        elif char == "[":
            brackets.append("]")
        else:
            if len(brackets) > 0:
                if char != brackets.pop():
                    return False
            else:
                return False

    return True if len(brackets) == 0 else False

print(isValid("{]"))
