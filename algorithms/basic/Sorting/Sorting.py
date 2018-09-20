# coding
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


    def QuickSort_2(self, arr):
        if len(arr) <= 1 :
            return arr

        if len(arr)>1:
            pivot = arr[0]
            less = []
            more = []
            equal = []
            for i in range(0,len(arr)):
                if arr[i]<pivot:
                    less.append(arr[i])
                elif arr[i]==pivot:
                    equal.append(arr[i])
                else:
                    more.append(arr[i])
            less = self.QuickSort_2(less)
            more = self.QuickSort_2(more)
            return self.QuickSort_2(less) + equal+ self.QuickSort_2(more)


    def QuickSort_1(self,arr,low,high):

        if(low < high):
            less,more = self.partition2(arr,low,high)
            # self.QuickSort_1(arr[:less])
            #
            # self.QuickSort_1(arr[more+1:])
            self.QuickSort_1(arr,low,less-1)
            self.QuickSort_1(arr,more,high)

    def partition2(self, arr,low,high):
        if len(arr) > 1:
            pivot = arr[high]
            print(pivot)
            less, more, cur = low-1, high+1,low
            while (cur < more):
                if arr[cur] < pivot:
                    arr[less+1], arr[cur] = arr[cur], arr[less+1]
                    cur += 1
                    less += 1
                    continue
                elif arr[cur] == pivot:

                    cur += 1

                else:

                    arr[more-1], arr[cur] = arr[cur], arr[more-1]
                    more -= 1
        return [less+1,more]


         # 返回==pivot的左右边界
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

    #
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
    # seq = [2, 0, 2,1, 49, 2,5,6,4,20, -8,7,1,2,3,4,0,-77,2]
    seq = [3,2,1,4,5]

    s = SortingSolution()

    # print(s.QuickSort_2(seq,0,len(seq)-1))
    # print(s.partition2(seq, 0, len(seq) - 1))
    print(s.QuickSort_1(seq,0,len(seq)-1))
    print(seq)
