arr=[1,2,2,3,4,4,4,4,4,4,4,5,6,6,7,7,7,8]
i=0
j=i+1
print("before two pointer:",arr)
for j in range(len(arr)):
    if arr[i]!=arr[j]:
        i=i+1
        arr[i]=arr[j]

print("aafter two pointer",arr[:i+1])