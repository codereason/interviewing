'''
168. Excel表列名称
给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。

例如：

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

示例 1：

输入：columnNumber = 1
输出："A"
示例 2：

输入：columnNumber = 28
输出："AB"
示例 3：

输入：columnNumber = 701
输出："ZY"
示例 4：

输入：columnNumber = 2147483647
输出："FXSHRXW"
 

提示：

1 <= columnNumber <= 231 - 1

'''
# class Solution:
#     def convertToTitle_NotFi(self, columnNumber: int) -> str:
#         res = ""
#         if columnNumber <=26: 
#             return chr(columnNumber+ord('A')-1)
        
#         while columnNumber // 26 >= 1:
#             yushu =  columnNumber%26
#             if yushu!= 0:
#                 res+=chr(yushu+ord('A')-1)

#             columnNumber = columnNumber-yushu
#             columnNumber = columnNumber//26
#         if columnNumber >0:
#             res+=chr(columnNumber+ord('A')-1)
#         return res[::-1]

# if __name__ == "__main__":
#     solu = Solution()
#     print(solu.convertToTitle_NotFi(676) )