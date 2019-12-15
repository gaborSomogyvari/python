
import sys
sys.setrecursionlimit(100000)
from decimal import *


#the function which calculates the square root
def iterator(SMALL,BIG,X):
    y=Decimal((SMALL+BIG)/Decimal(2))

    if y==SMALL or y==BIG:
        return y

    #if the result is correct
    if (y*y)==X:
        return y

    #if the result is too small
    if (y*y)<X:
        return iterator(y,BIG,X)

    #if the result is too big
    else:
        return iterator(SMALL,y,X)

#prepares the input to be processed
def preparation(number,digits):

    if number<=0:
        return "Please give another number to calculate with."
    if digits>1000:
        getcontext().prec=digits
    else:
        getcontext().prec=1000

    this=Decimal(iterator(Decimal(0),Decimal(number),Decimal(number)))
   
    
    if abs(this.as_tuple().exponent)  < digits and abs(this.as_tuple().exponent)!=0 :
        return this
    else:
        return round(this,digits)


if __name__=='__main__':

    while True:
        number=input("Please give me a number: ")
        digits=input("Please give me the digits: ")
        print("my result:")
        print(preparation(int(number),int(digits)))
        print("the built in sqr func() result:")
        print(Decimal(number).sqrt())






