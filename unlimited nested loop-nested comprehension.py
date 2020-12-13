# By Rouzbeh on Dec 12
#suppose length of n is al ot and you want to have all possble combinations:
# ['adg', 'adh', 'adi', 'aeg',......
# you cannot have lots of for inside each other especially if len(a) will change each time.
# so there are two ways to solve that as shwon here:


a=[["a","b","c"],["d","e","f"],["g","h","i"]]

#method 1
res=[""]
for i in range(len(a)):
    resTemp=[]
    for j in range(len(res)):
        for k in range(len(a[i])):
            resTemp.append(res[j]+a[i][k])
    res=resTemp

print(res)

#method 2 using nested comprehension
res=[""]
for i in range(len(a)):
    res=[item+char for item in res for char in a[i]]
print(res)