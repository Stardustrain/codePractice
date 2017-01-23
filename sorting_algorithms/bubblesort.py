import unittest


class BubbleSort(object):

    # 무조건 입력받은 배열의 길이만큼 sorting을 실행
    def bubble_sort(self, candidate_arr):
        for i in range(len(candidate_arr)):
            for index in range(len(candidate_arr)-1):
                if candidate_arr[index+1] < candidate_arr[index]:
                    candidate_arr[index+1], candidate_arr[index] = candidate_arr[index], candidate_arr[index+1]
        return candidate_arr

    # 정렬이 되었다고 판단되면 sorting을 멈춤
    def short_bubblesort(self, candidate_arr):
        switched = True
        passnum = len(candidate_arr) - 1
        while passnum > 0 and switched:
            for index in range(passnum):
                switched = False
                if candidate_arr[index+1] < candidate_arr[index]:
                    candidate_arr[index+1], candidate_arr[index] = candidate_arr[index], candidate_arr[index+1]
                    switched = True
            # sorting의 범위를 줄인다
            passnum -= 1
        return candidate_arr


class SortTest(unittest.TestCase):
    def test(self):
        b = BubbleSort()
        self.assertEqual([1, 2, 3, 5, 6, 7], b.bubble_sort([5, 2, 7, 1, 6, 3]))
        self.assertEqual([1, 2, 3, 5, 6, 7], b.short_bubblesort([5, 2, 7, 1, 6, 3]))


def main():
    t = SortTest()
    t.test()


if __name__ == "__main__":
    main()