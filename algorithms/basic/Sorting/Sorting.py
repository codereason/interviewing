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

        for i in range(len(A) - 1, -1, -1):
            for j in range(i):
                if (A[j] > A[j + 1]): A[j], A[j + 1] = A[j + 1], A[j]
        return A

    def SelectionSort(self, A):

        for i in range(len(A)):
            minIndex = i
            for j in range(i + 1, len(A)):
                if A[j] < A[minIndex]:
                    A[minIndex], A[j] = A[j], A[minIndex]
        return A

    def InsertionSort(self, A):

        for i in range(1, len(A)):
            for j in range(i - 1, -1, -1):
                if (j >= 0 and A[j] > A[j + 1]): A[j], A[j + 1] = A[j + 1], A[j]

        return A

    def QuickSort(self, A, begin, end):
        if len(A) > 1:
            split = self.partition2(A)
            self.QuickSort(A, begin, split)
            self.QuickSort(A, split + 1, end)

    def partition(self, arr, pivot):
        pass

    def partition2(self, arr):
        if len(arr) > 1:
            pivot = arr[0]
            less, more, cur = 0, len(arr) - 1, 0
            while (cur <= more):
                if arr[cur] < pivot:
                    arr[less], arr[cur] = arr[cur], arr[less]
                    cur += 1
                    less += 1
                    continue
                elif arr[cur] == pivot:

                    cur += 1

                else:

                    arr[more], arr[cur] = arr[cur], arr[more]
                    more -= 1

        return [less, more]  # 返回==pivot的左右边界
        # if arr==[]:
        #     return
        # i=0
        # j=len(arr)-1
        # k=0
        # while k<=j:#一开始用k<len(nums)出现了错误list index out of range
        #     if arr[k]==0:
        #         arr[k],arr[i]=arr[i],arr[k]
        #         k+=1
        #         i+=1
        #     elif arr[k]==2:
        #         arr[k],arr[j]=arr[j],arr[k]
        #         j-=1
        #     else:
        #         k+=1

    def ShellSort(self, A):
        pass

    def HeapSort(self, A):
        pass

    def MergeSort(self, A):
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

    def rightest_method(self, A):
        A.sort()




if __name__ == '__main__':
    seq = [2, 0, 1, 49, 20, -8]
    s = SortingSolution()
    print(s.partition2(seq))
    print(seq)
