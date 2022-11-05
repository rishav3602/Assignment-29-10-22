"""
2. write a function which  will be able to print an index of list element without using an index function
"""

l = ["a",67,90,"gh",78.09,"ris"]
def indexing(li):
    for i in range(0,len(li)) :
        print(li[i],": ",i)

k = indexing(l)
print(k)