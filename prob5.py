#5. write a function which will take input as a list with any kind of numeric value and give an out as a multiplication of 
#all the numeric data l = [3.5, 6.56, 4,5,"sudh" , "ineuron" , 'fsda bootcamp 2.0']

l = [3.5, 6.56, 4,5,"sudh" , "ineuron" , 'fsda bootcamp 2.0']
def test3(l):
    mul = 1
    for i in l :
        if type(i) == int or type(i) == float :
            mul = mul * i
    return mul

print(test3(l))