arr = [5, 4, 3, 2, 1]


def binary_search(nums, item):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (high + low) // 2
        if nums[mid] == item:
            return mid
        elif nums[mid] < item:
            high = mid - 1
        else:
            low = mid + 1
    return None


print(binary_search(arr, 1))
