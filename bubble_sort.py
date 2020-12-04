"""By Rouzbeh
   2020-12-01
    bubble sort
    https://www.geeksforgeeks.org/bubble-sort/
  """
from basics import *
from quick_sort import *

def bubble_sort(a):
    for i in range(len(a)):
        # -i because last i elements are already in place
        # -i because we are are comparing with next element
        for j in range(0, len(a)-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1], a[j]
    #return (a)

a = create_array(100,1000)
b=a
bubble_sort(a)
quicksort(b)

print(a)
print(b)

if a==b:
    print ("same")
else:
    print("Not Same")

