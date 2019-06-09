class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        f = (m+1)*[0]
        f[0]=0
        for i in range(len(A)):
            for j in range(m,1,-1):
                if j>=A[i]:
                    f[j] = max(f[j],f[j-A[i]]+A[i])
        return f[m]
        #二维数组的解法

    def backpack2(self,m,A):
        dp = 
  id

import pandas as pd
a = pd.read_csv(".csv")
import sklearn.tree