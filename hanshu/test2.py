# coding:utf-8
def add(a,b):
    c=a+b
    return c

def addd():
    a1=2
    a2=3
    return a1+a2


def adddd(a=9,b=8):#形参
     return a+b

def addddd(a=0,b=8):#形参
     return a+b

if __name__=="__main__":
     print (add(1,3))
     print addd()
     print adddd()
     print addddd(b=4,a=9)
