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
        total = list(range(1,n**2+1))
        cur = 0
        #border
        if n==1:
            return [[1]]
        res = [[0 for i in range(n)] for j in range(n)]
        l,u = 0,0
        r,d = n-1,n-1
        i,j=l,u
        while cur < len(total):
            
            while j <= r:
                res[i][j] = total[cur]
                cur+=1
                j+=1
            i+=1
            j-=1
            while i<=d:
                res[i][j] = total[cur]
                cur+=1
                i+=1
            j-=1
            i-=1
            while j>=l:
                res[i][j] = total[cur]
                cur+=1
                j-=1
            i-=1
            j+=1
            while i>=u+1:
                res[i][j] = total[cur]
                cur+=1
                i-=1
            i+=1
            j+=1
            r-=1
            d-=1
            l+=1
            u+=1
            
        # for i in res:
        #     print(i)
        return res

if __name__ == "__main__":
    N=2
    Solution().generateMatrix(N)