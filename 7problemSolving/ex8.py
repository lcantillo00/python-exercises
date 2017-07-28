def line(n):
    nl=''
    for i in range(n):
        nl+='#'
    return nl
def stairs(n):
    newstair=''
    for i in range(n):
        newstair+=(line(i)+'\n')
    return newstair

print(stairs(6))
