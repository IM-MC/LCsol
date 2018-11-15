class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip(' ')
        if str == '':
            return 0
        res = 0
        flag = 1
        if (str[0]<'0' or str[0]>'9') and (str[0] != '-' and str[0] != '+'):
            return 0
        else:
            if str[0] == '-':
                flag = -1
            elif str[0] == '+':
                flag = 1
            else:
                res = int(str[0])
            for i in range(1,len(str)):
                if str[i] == ' ' or str[i]<'0' or str[i]>'9':
                    break
                else:
                    res = res*10 + int(str[i])
        if flag==1:
            if res <= 2**31-1:
                return res
            return 2**31-1
        else:
            if res*flag >= -2**31:
                return res*flag
            return -2**31
