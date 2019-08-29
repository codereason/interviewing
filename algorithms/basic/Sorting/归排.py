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