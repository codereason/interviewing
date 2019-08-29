def InsertionSort(self, A):
    for i in range(1, len(A)):
        for j in range(i - 1, -1, -1):
            if (j >= 0 and A[j] > A[j + 1]): A[j], A[j + 1] = A[j + 1], A[
                j]

    return A