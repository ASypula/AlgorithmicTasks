from math import log, ceil


def printHeap(heap, size, k):  # k is a heap degree(2, 3, 4), size equals len(heap) - 1
    maxDepth = ceil(log((size), k)) # round log result up
    d = maxDepth # depth level, counting from 0
    d = 0
    while(d <= maxDepth):
        suma = 0
        for num in range(0, d):
            suma += k**num
        layerLength = suma + 1 # layerLengths stores number of index from which we start on every level
        line = ''
        for i in range(layerLength, layerLength + int(k**(d))):
            # print spaces only on not-last layer
            if(d != maxDepth):
                line += " " * int(k**(maxDepth - d))
            # more space for long lines
            loops = maxDepth - d
            if(loops >= k):
                loops -= k
                while(loops >= 0):
                    line += " " * (k**(loops))
                    loops -= 1
            if(i <= size): # check if its time to print heap element
                line += str(heap[i - 1])
            else:
                line += ("--") # if there is no node print '--'
            line += " " * int(k**(maxDepth - d))
            # more spaces for long lines
            loops = maxDepth - d
            if(loops >= k):
                loops -= k
                while(loops >= 0):
                    line += " " * int(k**(loops))
                    loops -= 1
        line += "\n"
        print(line)
        d += 1


heappp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
printHeap(heappp, 9, 2)
print("\n\n")
printHeap(heappp, 9, 3)
print("\n\n")
printHeap(heappp, 9, 4)
