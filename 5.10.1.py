# sort_utils.py
def bubbleSort(nlist):
    for passnum in range(len(nlist)-1, 0, -1):
        for i in range(passnum):
            if nlist[i] > nlist[i+1]:
                nlist[i], nlist[i+1] = nlist[i+1], nlist[i]
    return nlist
