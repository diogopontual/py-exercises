
def search(elements, value):
    left = 0
    right = len(elements) - 1
    while left <= right:
        mid = (left + right) // 2
        if (elements[mid] == value):
            return mid
        if (elements[mid] < value):
            left = mid + 1
        if (elements[mid] > value):
            right = mid - 1
