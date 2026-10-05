
k=4
arr=[1,2,3,2,22,1,44,66,5,43,45]
w=sum(arr[:k])
ms=w
for i in range(k,len(arr)):
    w=w+arr[i]
    w=w-arr[i-k]
    ms=max(ms,w)
print("max sum for fixed length k is:",ms)
