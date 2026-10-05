l=0
target=143
arr=[1,2,1,2,33,22,32,56,24,43,45,67,54,3,2,15]
w=0
ml=0
for r in range(len(arr)) :
    w=w+arr[r]
    while w>target:
        w=w-arr[l]
        l=l+1
    ml=max(ml,r-l+1)
print("variable max length:",ml)
    