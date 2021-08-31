
   2020-11-28
   This code is finding the first elements which is larger than
   https://www.youtube.com/watch?v=uEUXGcc2VXM&t=266s&ab_channel=AbdulBari


"""



def binarySearchIterative( list,target,low,high):
    while low<=high:
        mid = (high + low) // 2
        if list[mid] == target:
            return  mid
        if target<list[mid]:   #move to left
            high = mid - 1  # -1 is really important so the code works on ends
        else:                #move to right
            low = mid + 1  # +1 is really important so the code works on ends
    return "Not found"

def binarySearchIterativeNext( list,target,low,high):
    while low <= high:
        mid = (high + low) // 2
        if target < list[mid]:  # move to left
            high = mid - 1  # -1 is really important so the code works on ends
        else:  # move to right, so even if target=list[mid] gp rto right, so finally low will be mire than target
            low = mid + 1  # +1 is really important so the code works on ends
    return low     # if the targer number is the lat number in the list, the return would be one more


def binarySearchIterativeBefore (list,target,low,high):
    while low <= high:
        mid = (high + low) // 2
        if target <= list[mid]:  # move to left
            high = mid - 1  # -1 is really important so the code works on ends
        else:  # move to right
            low = mid + 1  # +1 is really important so the code works on ends
    return high     # if the targer number is the lat number in the list, the return would be one more



def binarySearchRecursion( list,target,low,high):
  if low >= high:
      if list[low]==target:
          return low
      else:
         return "NOT there"
  mid = (high + low) // 2
  if list[mid]==target:
      return mid
  if target>list[mid]:
      return binarySearchRecursion(list,target,mid+1,high)  # +1 is really important so the code works on ends
  else:
      return binarySearchRecursion(list, target, low, mid-1)  # -1 is really important so the code works on ends






list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
target=25
high=len(list)-1
print(binarySearchIterative(list,target,0,high))
print(binarySearchRecursion(list,target,0,high))
print(binarySearchIterativeNext(list,target,0,high))
print(binarySearchIterativeBefore(list,target,0,high))

list=[0,1,5,5,5,5,6,7,8,9,10,11,12,13,14,15]
target=5
high=len(list)-1
print(binarySearchIterative(list,target,0,high))
print(binarySearchRecursion(list,target,0,high))
print(binarySearchIterativeNext(list,target,0,high))
print(binarySearchIterativeBefore(list,target,0,high))



