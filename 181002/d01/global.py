# yangli

a= 1

def printa():
    global  a



    print(a)
    a=100
    print(a)

def getss(a,*b):
    print(a)
    print(b)
   # print(c)
    print(a, b)
    #print(a,b,c)

printa()
print(a)
getss(1,2,3,4,5,6,7,8)