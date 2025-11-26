#buble_sort
def bubble_sort(l):
    x = len(l)
    s = 0
    for i in range(x):
        swapped = False
        for j in range(0,x-i-1):
            if l[j] > l[j+1]:
               l[j], l[j+1] = l[j+1], l[j]
               s += 1
               swapped = True
        if not swapped:
            break
    return l
print(bubble_sort([3,5,6,23,8,9,12]))