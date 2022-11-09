class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res=[]
        for i,n in enumerate(nums):
            if i>0 and n==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while(l<r):
                t_sum=n+nums[l]+nums[r]
                if t_sum>0:
                    r-=1
                elif t_sum<0:
                    l+=1
                else:
                    res.append([n,nums[l],nums[r]])
                    l+=1
                    while(nums[l]==nums[l-1] and l<r):
                        l+=1
        return res