def counting(alist):
    sum=0
    for i in alist:
        if len(i)==5:
             sum+=1
    return sum
alist=["lol", "lololololo","fdhghdss"]
print(counting(alist))
