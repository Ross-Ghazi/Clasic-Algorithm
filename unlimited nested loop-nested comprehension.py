
#suppose length of n is a lot and you want to have all possble combinations:
# ['adg', 'adh', 'adi', 'aeg',......
# you cannot have lots of for loops inside each other especially if len(a) will change each time.
# so there are two ways to solve that iteratively and one way to solve it recursively  as shown here.
# no reference but look at the video here:
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/solution/


a=[["a","b","c"],["d","e","f"],["g","h","i"]]

#method 1
res=[""] # if you put [] then j loop will not start
for i in range(len(a)):
    resTemp=[]
    for j in range(len(res)):
        for k in range(len(a[i])):
            resTemp.append(res[j]+a[i][k])
    res=resTemp

print(res)

#method 2 using nested comprehension
res=[""] # if you put []  the loop will not work
        #(len(res))=1 which is ewual with length of ["A"]
for i in range(len(a)):
    res=[j+k for j in res for k in a[i]]
print(res)

#method 3 recursive
def backtrack(sofar,a):
    if len(a)==0:
        output.append(sofar)
    else:
        for k in range(len(a[0])):
             backtrack(sofar+a[0][k],a[1:])
output=[]

backtrack("",a)
print(output)
