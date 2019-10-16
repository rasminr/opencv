"""
sdfdsf
dfd
"""

gg3=9#gg3 is a global variable
def gg1():
    #global gg, gg is not a global variable
    gg=gg3+1#gg is a local variable of gg1 fucntion
    print(gg)
def hh():
    gg1()
    print(gg)  
hh()      
pr