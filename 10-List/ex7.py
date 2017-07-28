def sum_neg(xs):
    result=0
    for i in xs:
        if i<0:
            result+=i
    return result
print(sum_neg([-2,3,-4]))
