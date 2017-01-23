import unittest


class QuickSort(object):

    def change_pivot(self, arr):
        low = (0, arr[0])
        middle = (int(len(arr)/2), arr[int(len(arr)/2)])
        high = (len(arr)-1, arr[len(arr)-1])
        pivot_arr = [low, middle, high]
        pivot_arr.sort(key=lambda x: x[1])

        arr[0] = pivot_arr[1][1]
        arr[pivot_arr[1][0]] = low[1]

        return arr

    def quick_sort(self, arr):
        return self._quick_sort_exchange(arr, 0, len(arr)-1)

    def _quick_sort_exchange(self, candidate_arr, start, end):
        if start < end:
            split_point = self._partition(candidate_arr, start, end)

            self._quick_sort_exchange(candidate_arr, start, split_point-1)
            self._quick_sort_exchange(candidate_arr, split_point+1, end)

        return candidate_arr

    def _partition(self, candidate_arr, start, end):
        pivot = candidate_arr[start]
        low = start + 1
        high = end

        while low <= high:
            while low <= high and candidate_arr[low] < pivot:
                low += 1
            while candidate_arr[high] > pivot and low <= high:
                high -= 1

            if low <= high:
                candidate_arr[low], candidate_arr[high] = candidate_arr[high], candidate_arr[low]

        candidate_arr[start], candidate_arr[high] = candidate_arr[high], candidate_arr[start]

        return high


class SortTest(unittest.TestCase):
    def test(self):
        q = QuickSort()
        self.assertEqual([1, 2, 3, 5, 6, 7], q.quick_sort([5, 2, 7, 1, 6, 3]))
        # failure Test
        # self.assertEqual([1, 2, 3, 4, 8, 9], q.quick_sort([5, 2, 7, 1, 6, 3]))


def main():
    t = SortTest()
    t.test()


if __name__ == "__main__":
    main()