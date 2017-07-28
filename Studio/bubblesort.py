def bubble_sort(a_list):
    is_sorted = False
    while is_sorted == False:
        num_swaps = 0
        for i in range(0, len(a_list) - 1):
            a = a_list[i]
            b = a_list[i+1]
            if a > b:
                a_list[i] = b
                a_list[i+1] = a
                num_swaps = num_swaps + 1
        if num_swaps == 0:
            is_sorted = True
    return a_list

bubble_sort([3,2,1])

j=24
print(j%2)
