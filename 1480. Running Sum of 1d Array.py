class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        i = 0
        for v in nums:
            if runningSum == []:
                runningSum.append(v)
            else:
                value = runningSum[i] + v
                runningSum.append(value)
                i += 1
        return runningSum