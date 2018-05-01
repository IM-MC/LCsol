def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """

    index = -1
    digit = digits[index]

    if digit == 9:
        while digit == 9:
            digits[index] = 0
            if len(digits) + index != 0:
                index -= 1
                digit = digits[index]
            else:
                digits.insert(0, 1)
                return digits

    digits[index] += 1
    return digits

print(plusOne([1,3,3]))
