class Solution:
    def twoSum(self, nums, target):
        for index1,i in enumerate(nums):
            num2=target-i
            for index2 in range(index1+1,len(nums)):
                if num2==nums[index2]:
                    return [index1,index2]

sol=Solution()
print(sol.twoSum([3,2,4],6))