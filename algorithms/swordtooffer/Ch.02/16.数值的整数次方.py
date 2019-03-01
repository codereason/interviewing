class Solution:
    def Power(self, base, expo):
        # write code here

        if expo == 1:
            return base
        if expo == 0:
            return 1
        if expo < 0:
            return 1 / self.Power(base, -1 * expo)
        if (expo % 2 == 0):
            return self.Power(base ** 2, expo / 2)
        else:
            return base * self.Power(base ** 2, (expo - 1) / 2)