from typing import List
def sumsOfSubsets(arr:List[int],ans:List,l:int,r:int,sum=0):
    if l>r:
        ans.append(sum)
        return 
    sumsOfSubsets(arr,ans,l+1, r, sum+arr[l])
    sumsOfSubsets(arr,ans,l+1, r, sum)
    
arr = list(map(int,input().split()))
ans = []

sumsOfSubsets(arr,ans,0,len(arr)-1,sum=0)
print(ans)