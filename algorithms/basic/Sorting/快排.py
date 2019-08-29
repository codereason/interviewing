def QuickSort_2(self, arr):
    if len(arr) <= 1:
        return arr

    if len(arr) > 1:
        pivot = arr[0]
        less = []
        more = []
        equal = []
        for i in range(0, len(arr)):
            if arr[i] < pivot:
                less.append(arr[i])
            elif arr[i] == pivot:
                equal.append(arr[i])
            else:
                more.append(arr[i])
        # less = self.QuickSort_2(less)
        # more = self.QuickSort_2(more)
        return self.QuickSort_2(less) + equal + self.QuickSort_2(more)


def QuickSort_1(self, arr, low, high):
    if (low < high):
        less, more = self.partition2(arr, low, high)
        # self.QuickSort_1(arr[:less])
        #
        # self.QuickSort_1(arr[more+1:])
        self.QuickSort_1(arr, low, less - 1)
        self.QuickSort_1(arr, more, high)


def partition2(self, arr, low, high):
    if len(arr) > 1:
        pivot = arr[high]
        print(pivot)
        less, more, cur = low - 1, high + 1, low
        while (cur < more):
            if arr[cur] < pivot:
                arr[less + 1], arr[cur] = arr[cur], arr[less + 1]
                cur += 1
                less += 1
                continue
            elif arr[cur] == pivot:

                cur += 1

            else:

                arr[more - 1], arr[cur] = arr[cur], arr[more - 1]
                more -= 1
    return [less + 1, more]