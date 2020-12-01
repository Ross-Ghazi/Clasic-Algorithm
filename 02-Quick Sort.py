"""By Rouzbeh
   2020-11-30
  Quick sort two methods
  https://www.youtube.com/watch?v=RFyLsF9y83c&t=344s&ab_channel=BrianFaure
  https://www.youtube.com/watch?v=1Mx5pEeTp3A&t=278s&ab_channel=BrianFaure
  https://www.youtube.com/watch?v=MZaf_9IZCrc
  """

from random import randint

def create_array(size=10,max=50):   # create random array as input
    return[randint(-max,max)  for _ in range(size)]

def quicksort(a):                   #Not in place algorithm
    if len(a)<=1: return a
    smaller, equal,larger=[],[],[]
    pivot=a[randint(0,len(a)-1)]

    for x in a:
        if x<pivot:      smaller.append(x)
        elif x==pivot:   equal.append(x)
        else:    larger.append(x)

    return quicksort(smaller)+equal+quicksort(larger)



def partition(a, low, high):    #for use in place algorithm
   i=low-1

   random_indx = randint(low, high)
   a[high], a[random_indx] = a[random_indx], a[high]

   pivot=a[high]


   for j in range(low, high):
       if a[j]<= pivot:
           i+=1
           a[i],a[j]=a[j],a[i]

   a[i+1],a[high]=a[high],a[i+1]
   return i+1


def quicksort_inplace(a,low=0, high=None):
    if high==None:
        high=len(a)-1
    if low<high:
        p_indx=partition(a,low,high)
        quicksort_inplace(a,low,p_indx-1)
        quicksort_inplace(a,p_indx+1,high)
















a=create_array(10,10)
b=a
print("a                  :",a)
c=quicksort(a)
print("Quicksort          :",c)
quicksort_inplace(b)
print("Quicksort_inplace  :",b)

if b==c:
    print ("Results are the same")
else: print("Results are NOT the same")

