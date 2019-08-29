def BubbleSort(self, A):
    '''
 i∈[0,N-1)               //循环N-1遍
   j∈[0,N-1-i)           //每遍循环要处理的无序部分
     swap(j,j+1)          //两两排序（升序/降序）
     '''

    for i in range(len(A) - 1, -1, -1):
        for j in range(i):
            if (A[j] > A[j + 1]): A[j], A[j + 1] = A[j + 1], A[j]
    return A