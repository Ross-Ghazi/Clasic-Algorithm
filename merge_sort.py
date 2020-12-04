"""By Rouzbeh
   2020-11-30
    merge sort
    https://www.youtube.com/watch?v=3aTfQvs-_hA&ab_channel=BrianFaure
  """

from random import randint
from time import time
def create_array(size=10,max=50):   # create random array as input
    return[randint(0,max)  for _ in range(size)]



def merge(a,b):
    c=[]
    i=0
    j=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j += 1
    if i==len(a): c.extend(b[j:])    # Always either i or j will reach to the end
    # It is not possible to get both of them to the end so either if
    # or else should be applied.
    else:              c.extend(a[i:])
    return c
def merge_sort(a):
    if len(a)<=1: return a
    # the video is using / rather than // which gives an error
    left,right=merge_sort(a[:len(a)//2]),merge_sort(a[len(a)//2:])
    return merge(left,right)

n=[10,100,1000,10000]
times=[]
for size in n:
    a=create_array(size,size)
    t0=time()
    merge_sort(a)
    t1=time()
    times.append(t1-t0)


print(times)




