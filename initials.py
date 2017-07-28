def getinitial(fullname):
    sum=""
    result=fullname.split(' ')
    for i in result:
        sum=sum+i[:1].upper()
    return sum
print(getinitial("lili  neto cantillo"))
