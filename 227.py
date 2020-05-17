def calculate(s):
    """
    :type s: str
    :rtype: int
    """

    s += "+0"

    num, stack, op = 0, [], "+"
    for i in range(len(s)):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        elif not s[i].isspace():
            if op == "+":
                stack.append(num)
            elif op == "-":
                stack.append(-num)
            elif op == "*":
                stack.append(stack.pop() * num)
            elif op == "/":
                stack.append(int(stack.pop() / num))

            op = s[i]
            num = 0

    return sum(stack)


print(calculate("14-3/2"))
