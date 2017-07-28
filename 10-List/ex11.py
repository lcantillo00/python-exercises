def sum_of_initial_odds(nums):
    sum=0
    for i in nums:
        if i%2 !=0:
            sum=sum+i
        else:
            break
    return sum


from test import testEqual

testEqual(sum_of_initial_odds([1,3,1,4,3,8]), 5)
testEqual(sum_of_initial_odds([6,1,3,5,7]), 0)
testEqual(sum_of_initial_odds([1, -7, 10, 23]), -6)
testEqual(sum_of_initial_odds(range(1,555,2)), 76729)
