# from test import testEqual
#
# def remove(substr,theStr):
#     # your code here
#     strIndex=theStr.find(substr)
#     if strIndex<0:
#         return theStr
#     else:
#         newstring=theStr[:strIndex]+theStr[strIndex+len(substr):]
#         return newstring
#
#
# testEqual(remove('an', 'banana'), 'bana')
# testEqual(remove('cyc', 'bicycle'), 'bile')
# testEqual(remove('iss', 'Mississippi'), 'Missippi')
# testEqual(remove('egg', 'bicycle'), 'bicycle')
# testEqual(remove('oo', 'Yahoohoo'), 'Yahhoo')
# ///////////////////////////////////////
from test import testEqual

def reverse(text):
    w=''
    for x in text:
        w=x+w
    return w

testEqual(reverse("happy"), "yppah")
testEqual(reverse("Python"), "nohtyP")
testEqual(reverse(""), "")
