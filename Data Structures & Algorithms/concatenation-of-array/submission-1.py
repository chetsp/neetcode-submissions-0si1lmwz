class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        length = len(nums)
        ans = nums+nums
        return ans       