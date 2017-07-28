def line(n):
    st=''
    for i in range(n):
        st+="#"
    return st
def rectangle(n):
    side=''
    for i in range(n):
        side=side+ (line(n)+'\n')
    return side
print(rectangle(6))
