import unittest


def insertsort(candidate_arr):
    for i in range(len(candidate_arr)):
        index = i
        cur_val = candidate_arr[index]

        while index > 0 and candidate_arr[index-1] > cur_val:
            candidate_arr[index] = candidate_arr[index-1]
            index -= 1
        candidate_arr[index] = cur_val


class SortTest(unittest.TestCase):
    def test(self):
        self.assertEqual([1, 2, 3, 5, 6, 7], insertsort([5, 2, 7, 1, 6, 3]))


def main():
    t = SortTest()
    t.test()


if __name__ == "__main__":
    main()