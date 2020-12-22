'''
59. 螺旋矩阵 II

给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
[
 [ 1, 2, 3,4 ],
 [ 12, 13, 14,5],
 [ 11,16, 15 ,6],
 [ 10, 9, 8 ,7]
]

'''

class Solution:
    def generateMatrix(self, n):
        total = n**2
        cur = 0
        #border
        l,u = 0,0
        r,d = n-1,n-1
        while cur < total:
            
        
        return None

if __name__ == "__main__":
    N=8
    print(Solution().generateMatrix(N))