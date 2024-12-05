# search_utils.py
def Sequential_Search(dlist, item):
    for index, element in enumerate(dlist):
        if element == item:
            return (True, index)
    return (False, -1)
