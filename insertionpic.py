import cv2
import numpy as np
import threading
back = cv2.imread('tback.jpg')
front = cv2.imread('fullim.jfif')
back = cv2.resize(back, (1200, 600))
front = cv2.resize(front, (1200, 600))
length = front.shape[0]
breadth = front.shape[1]
sublen = length//10
subbre = breadth//10
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


def clr():
    totimg = dispr(arr)
    back[0:, 0:] = totimg[0:, 0:]
    cv2.imshow('insertion', back)
    global qz
    if qz == 0:
        cv2.waitKey(5000)
        qz = 1
    else:
        cv2.waitKey(1)
    larr = list(arr)
    larr.sort()
    if larr == arr:
        cv2.waitKey(0)
        exit()


def insertion_sort(arr):
    for x in range(1, len(arr)):
        val = arr[x]
        y = x-1
        while y >= 0 and arr[y] > val:
            arr[y+1] = arr[y]
            y -= 1
        arr[y+1] = val
        clr()


sublen = length//10
subbre = breadth//10
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


def clr():
    totimg = dispr(arr)
    back[0:, 0:] = totimg[0:, 0:]
    cv2.imshow('insertion', back)
    global qz
    if qz == 0:
        cv2.waitKey(5000)
        qz = 1
    else:
        cv2.waitKey(1)
    larr = list(arr)
    larr.sort()
    if larr == arr:
        cv2.waitKey(0)
        exit()


def insertion_sort(arr):
    for x in range(1, len(arr)):
        val = arr[x]
        y = x-1
        while y >= 0 and arr[y] > val:
            arr[y+1] = arr[y]
            y -= 1
        arr[y+1] = val
        clr()


t1 = threading.Thread(target=insertion_sort, args=(arr,))
t1.start()
