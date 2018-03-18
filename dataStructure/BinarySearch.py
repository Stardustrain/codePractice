class BinarySearch:
    sorted_list = []

    def __init__(self, sorted_list):
        self.sorted_list = sorted_list

    def search(self, search_value):
        sorted_list = self.sorted_list

        if len(sorted_list) == 0:
            return False

        low = 0
        high = len(sorted_list) - 1

        while low <= high:
            mid = (high + low) // 2

            if sorted_list[mid] == search_value:
                return search_value

            if search_value > sorted_list[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return False
