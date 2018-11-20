def intToRoman(self, num):
        roman = [
            ['I', 'V'],
            ['X', 'L'],
            ['C', 'D'],
            ['M']
        ]

        count = 0
        result = ''
        while num > 0:
            digit = num%10
            if count == 3:  # for digit in Thousands place
                temp = roman[count][0] * digit
            else:
                if digit < 4:
                    temp = roman[count][0] * digit
                elif digit == 4:
                    temp = roman[count][0] + roman[count][1]
                elif digit == 9:
                    temp = roman[count][0] + roman[count + 1][0]
                else:
                    temp = roman[count][1] + roman[count][0] * (digit-5)
            num = num//10
            count += 1
            result = temp + result
        return result
