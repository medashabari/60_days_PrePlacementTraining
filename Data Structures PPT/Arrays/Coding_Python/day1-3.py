class GetMaxProduct:
    def get_max_product(self,arr:list,n:int) -> int:
        if n==0:
            return 0
        max_so_far = arr[0]
        min_so_far = arr[0]
        result = max_so_far

        for i in range(1,n):
            curr = arr[i]
            # if we cannot use temp here then in next line the min_so_far value can change
            temp_max = max(curr,max_so_far*curr,min_so_far*curr) 
            min_so_far = min(curr,max_so_far*curr,min_so_far*curr)

            max_so_far = temp_max 

            result = max(max_so_far,result)
        return result
arr = list(map(int,input().split()))
obj = GetMaxProduct()
print(f'Maximum sub-array product is {obj.get_max_product(arr,len(arr))}')