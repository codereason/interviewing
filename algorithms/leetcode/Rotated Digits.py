class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        for i in range(1, N + 1):
            List = []
            while (i):
                num = i % 10
                List.append(num)
                i = i / 10
            Flag = False
            if 3 not in List and 4 not in List and 7 not in List:
                for t in List:
                    if (t == 2 or t == 5 or t == 6 or t == 9):
                        Flag = True
            if Flag == True: count = count + 1
        return count
