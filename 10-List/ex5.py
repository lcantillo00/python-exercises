import random
def max(alist):
    maxnum=0
    for i in alist:
        if maxnum<i:
            maxnum=i
    return maxnum
def main():
    f=[]
    for i in range(100):
        f.append(random.randint(0, 1000))
    print(max(f))
if __name__=="__main__":
    main()
