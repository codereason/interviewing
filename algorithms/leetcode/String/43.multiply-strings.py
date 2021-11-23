'''
43. 字符串相乘
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
通过次数180,646提交次数402,254
'''

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
         
        length = len(num2) 
        list = []
        for i in range(len(num2)):
            list.append( pow(10,length- i - 1) * self.multiply_single_digit(num1,num2[i] ) )
        return str(sum(list))
    def multiply_single_digit(self,num1,num2):
        '''
        num1 任意位数
        Num2 必须是一位数
        '''
        length = len(num1)
        list = []
        for i in range(len(num1)):
            list.append(int(num1[i])* int(num2) * pow(10,length- i - 1))         
        return sum(list)

if __name__ == "__main__":
    s = Solution()
    n = "2"
    n2 = "3"
    print(s.multiply(n,n2))
