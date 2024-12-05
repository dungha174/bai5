# search_utils.py
def binary_search(lst, value):
    low = 0
    high = len(lst) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == value:
            return True
        elif lst[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return False
