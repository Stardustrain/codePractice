def insertsort(candidate_arr):
    for i in range(len(candidate_arr)):
        index = i
        cur_val = candidate_arr[index]

        while index > 0 and candidate_arr[index-1] > cur_val:
            candidate_arr[index] = candidate_arr[index-1]
            index -= 1
        candidate_arr[index] = cur_val


arr = [5, 6, 8, 1, 3, 2]
insertsort(arr)
print(arr)