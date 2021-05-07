from math import log, ceil


def printHeap(heap, size, k):  # k to stopien heap (2, 3, 4), size to liczba el w tablicy - 1
    maxDepth = ceil(log((size), k))
    d = maxDepth
    while(d >= 0):
        suma = 0
        for num in range(0, d):
            suma += k**num
        layerLength = suma + 1
        line = ''
        for i in range(layerLength, layerLength + int(k**(d))):
            # before spaces only on not-last layer
            if(d != maxDepth):
                line += " " * int(k**(maxDepth - d))
            # extra spaces for long lines
            loops = maxDepth - d
            if(loops >= k):
                loops -= k
                while(loops >= 0):
                    line += " " * (k**(loops))
                    loops -= 1
            # add in the number
            if(i <= size):
                line += str(heap[i - 1])
            else:
                line += ("--")
            line += " " * int(k**(maxDepth - d))
            # extra spaces for long lines
            loops = maxDepth - d
            if(loops >= k):
                loops -= k
                while(loops >= 0):
                    line += " " * int(k**(loops))
                    loops -= 1
        line += "\n"
        print(line)
        d -= 1


heappp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
printHeap(heappp, 9, 4)
#print(ceil(log((10), 3)))

