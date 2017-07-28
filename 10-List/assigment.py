# TODO
# # define a function called sum_evens, which receives one argument, a list of numbers.
# # your function should return the sum of all the even numbers in the list
# def sum_evens(listnum):
#     theSum = 0
#     for i in listnum:
#         if i%2==0:
#             theSum = theSum + i
#     return theSum



# # don't copy these tests into Vocareum
# from test import testEqual

# testEqual(sum_evens([2,3,4]), 6)
# testEqual(sum_evens([]), 0)
# testEqual(sum_evens([0,7,2,4,2,1]), 8)
# testEqual(sum_evens([0,1,2,3,4,5,6,7,8,9]), 20)
# testEqual(sum_evens(range(200,500)), 52350)
# ////////////////////////////////////////////////////////////

def get_country_codes(prices):
    # your code here
    newl=prices.split(', ')
    new_arr = []
    
    for i in newl:
        pos=i.index("$")
        re=i[:pos]
        new_arr.append(re)
    return ",".join(new_arr)




