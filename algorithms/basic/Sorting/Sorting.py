class SortingSolution:
    """
    @param: A: an integer array
    @return: 
    """

    def BubbleSort(self, A):
        '''
     i∈[0,N-1)               //循环N-1遍
       j∈[0,N-1-i)           //每遍循环要处理的无序部分
         swap(j,j+1)          //两两排序（升序/降序）
         '''

        for i in range(len(A)-1,-1,-1):
            for j in range(i):
                if(A[j]>A[j+1]):A[j],A[j+1]=A[j+1],A[j]
        return A


    def SelectionSort(self,A):

        for i in range(len(A)):
            minIndex = i
            for j in range(i+1,len(A)):
                if A[j]<A[minIndex]:
                    A[minIndex],A[j] = A[j],A[minIndex]
        return A

    def InsertionSort(self,A):

        for i in range(1,len(A)):
            for j in range(i-1,-1,-1):
                if(j>=0 and A[j]>A[j+1]):A[j],A[j+1]=A[j+1],A[j]

        return A

    def QuickSort(self,A):
        pass


    def ShellSort(self,A):
        pass


    def HeapSort(self,A):
        pass


    def MergeSort(self,A):
        if len(A) > 1:

            mid = int(len(A) / 2)
            left, right = A[:mid], A[mid:]
            self.MergeSort(left)
            self.MergeSort(right)
            '''
            mergeing left and right
            '''

            i, j, k = 0, 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    A[k] = left[i]
                    k += 1
                    i += 1
                else:
                    A[k] = right[j]
                    k += 1
                    j += 1

            while i < len(left):
                A[k] = left[i]
                k += 1
                i += 1

            while j < len(right):
                A[k] = right[j]
                k += 1
                j += 1

    def right_method(self,A):
        A.sort()


if __name__ == '__main__':
    seq = [4, 5, 7, 9, 7, 5, 1, 0, 7, -2, 3, -99, 6]
    s = SortingSolution()
    s.MergeSort(seq)
    print(seq)