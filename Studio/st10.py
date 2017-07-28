def sum_of_roll(double_list):
    # Your code here
    newlist=[]

    for row in range (len(double_list)):
        total = 0
        for col in range(len(double_list[row])):
            total += double_list[row][col]

        newlist.append(total)

    return newlist

print(sum_of_roll( [[4, 5, 2], [6,2,1], [4,4,4]] ))
print(sum_of_roll([[3, 4, 6],[2,6,1],[3,4,3]]))
