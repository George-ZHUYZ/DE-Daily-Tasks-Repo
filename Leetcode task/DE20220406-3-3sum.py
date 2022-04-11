class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        nums.sort()

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                value = nums[i] + nums[j] + nums[k]
                if (value == 0):
                    output.append([nums[i], nums[j], nums[k]])
                    j += 1
                elif (value < 0):
                    j += 1
                else:
                    k -= 1

        finalOutput = []

        for a in output:
            if a not in finalOutput:
                finalOutput.append(a)

        return finalOutput
