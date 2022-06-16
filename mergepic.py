import cv2
import numpy as np
import threading
back = cv2.imread('tback.jpg')
front = cv2.imread('fullim.jfif')
back = cv2.resize(back, (1200, 600))
front = cv2.resize(front, (1200, 600))
length = front.shape[0]
breadth = front.shape[1]
sublen = length//15
subbre = breadth//15
i = 0
k = 0
m = 0
lol = 0

for x in range(0, length, sublen):  # img split and store
    k += 1
    for y in range(0, breadth, subbre):
        if x == 0:
            m += 1
        i += 1
        cv2.imwrite('subdirect/'+str(i)+'.jpg', front[x:x+sublen, y:y+subbre])
        lol += 1
print(m, lol, i)


def dispr(arr):
    cntr = 2  # joins sub
    totimg = cv2.imread('subdirect/'+str(1)+'.jpg')
    for x in range(1, i, m):
        tp = 0
        if x != 1:
            fimg = cv2.imread('subdirect/'+str(arr[x-1])+'.jpg')
        for y in range(2, m+1):
            timg = cv2.imread('subdirect/'+str(arr[cntr-1])+'.jpg')
            if x == 1:
                totimg = np.concatenate((totimg, timg), axis=1)
            else:
                fimg = np.concatenate((fimg, timg), axis=1)
            cntr += 1
        cntr += 1
        if x != 1:
            totimg = np.concatenate((totimg, fimg), axis=0)
    return totimg


arr = [x for x in range(1, lol+1)]
np.random.shuffle(arr)
tarr = list(arr)
mkarr = list(arr)
qz = 0
mz = 0


def mlr(arrt):
    tot = dispr(arrt)
    back[0:, 0:] = tot[0:, 0:]
    cv2.imshow('merge', back)
    global mz
    if mz == 0:
        cv2.waitKey(5000)
        mz = 1
    else:
        cv2.waitKey(1)
    mtt = list(arrt)
    mtt.sort()
    if mtt == arrt:
        cv2.waitKey(0)


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:

        m = l+(r-l)//2

        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
        mlr(arr)


t2 = threading.Thread(target=mergeSort, args=(tarr, 0, len(tarr)-1,))

t2.start()
