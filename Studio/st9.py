def bubble_sort(alist):
    is_sorted=False
    while is_sorted==False:
            num_swap=0
            for passnum in range(len(alist)-1,0,-1):
                for i in range(passnum):
                    if alist[i]>alist[i+1]:
                        temp = alist[i]
                        alist[i] = alist[i+1]
                        alist[i+1] = temp
                        num_swap=num_swap+1
            if num_swap==0:
                is_sorted=True
    return alist
print((bubble_sort([0]), [0]))
print(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
print((bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5]))
print((bubble_sort([4, 5, 3, 1, 2]), [1, 2, 3, 4, 5]))
