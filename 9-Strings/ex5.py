# from test import testEqual
#
# def remove_all(substr,theStr):
#      newstring=theStr.replace(substr,"",)
#      return newstring
#
#
# testEqual(remove_all('an', 'banana'), 'ba')
# testEqual(remove_all('cyc', 'bicycle'), 'bile')
# testEqual(remove_all('iss', 'Mississippi'), 'Mippi')
# testEqual(remove_all('eggs', 'bicycle'), 'bicycle')
#
# from test import testEqual
# ///////////////////////////////////////////////////////////s
def is_palindrome(text):
    # your code here
    left=0
    rigth=len(text)-1
    while left<=rigth:
        if text[left]==text[rigth] or text=="":
            return True
        else:
            left+=1
            rigth+=1
            return False
testEqual(is_palindrome('abba'), True)
testEqual(is_palindrome('abab'), False)
testEqual(is_palindrome('straw warts'), True)
testEqual(is_palindrome('a'), True)
testEqual(is_palindrome(''), True)
