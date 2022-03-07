class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.mainCode(candidates,target,[],[],0,0)
        
    def mainCode(self,candidates,target,mat,arr,sum,index):
        if sum==target:
            mat.append(arr.copy())
            return mat
        for i in range(index,len(candidates)):
            if sum+candidates[i]>target:
                return mat
            arr.append(candidates[i])
            mat=self.mainCode(candidates,target,mat,arr,sum+candidates[i],i)
            arr.pop()
        return mat

        
sol=Solution()
print(sol.combinationSum([2,3,5],8))