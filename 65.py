def plusOne(self, digits: List[int]) -> List[int]:
    add1 = True
    digits.insert(0, 0)
    print(digits)

    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9 and add1:
            digits[i] = 0
        elif add1:
            digits[i] += 1
            add1 = False

    return digits[1:] if digits[0] == 0 else digits
