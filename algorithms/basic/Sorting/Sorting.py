class SortingSolution:
    """
    @param: A: an integer array
    @return: 
    """
    def BubbleSort(self, A):
        # write your code here
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                if A[i]>A[j]:A[i],A[j]=A[j],A[i]

    def SelectionSort(self,A):
        for i in range(len(A)):
            minIndex = i
            for j in range(i+1,len(A)):
                if A[j]<A[minIndex]:
                    A[minIndex],A[j] = A[j],A[minIndex]

    def InsertionSort(self,A):
        pass

    def QuickSort(self,A):
        pass

    def ShellSort(self,A):
        pass


    def HeapSort(self,A):
        pass

    def MergeSort(self,A):
        pass
