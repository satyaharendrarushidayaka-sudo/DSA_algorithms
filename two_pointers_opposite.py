arr=[1,2,4,6,8,8,9,19,80]
l=0
target=10
r=len(arr)-1
while l<r:
    two_sum=arr[l]+arr[r]
    if two_sum==target:
        print([l,r])
        l=l+1
        
        
    elif two_sum<target:
        l=l+1
    else:
        r=r-1
