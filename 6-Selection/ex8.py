# from test import testEqual
#
# def is_odd(n):
#     if(n%2 !=0):
#         return True
#     else:
#         return False
#
# testEqual(is_odd(10), False)
# testEqual(is_odd(5), True)
# testEqual(is_odd(1), True)
# testEqual(is_odd(0), False)
def pick_activity(a,b):

    if a=="hot" and b=="wet":
        msg="Watch Neflix"
    elif a=="hot" and b=="dried":
        msg= "go swiming"
    elif a=="cold" and b=="wet":
        msg="go paint"
    elif a=="cool" and b=="dried":
        msg ="go to a a cafe and read"
    return msg

print (pick_activity("hot","wet"))
