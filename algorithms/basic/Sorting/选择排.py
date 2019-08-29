def SelectionSort(self, A):
    for i in range(len(A)):
        minIndex = i
        for j in range(i + 1, len(A)):
            if A[j] < A[minIndex]:
                A[minIndex], A[j] = A[j], A[minIndex]
    return A
