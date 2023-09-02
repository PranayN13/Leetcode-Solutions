class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.dfs(candidates,target,0,[],result)
        return result

    def dfs(self, nums, target, index, path, result):
        if target < 0:
            return 
        if target == 0:
            result.append(path)
        for i in range(index,len(nums)):
            self.dfs(nums,target-nums[i],i,path+[nums[i]],result)