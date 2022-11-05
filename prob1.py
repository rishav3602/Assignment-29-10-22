"""
1. write a function which will try to find out len of a string without using an inbuilt len function 

"""

def length (l):
    count = 0 
    for i in l :
        print (i)
        if type(i) == str :
            count = count + 1
    return count

k = length("rishav")
print(k)
 
m = length("kumar")
print(m)

n = length("operations of ram")
print(n)