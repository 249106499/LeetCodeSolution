"""给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。"""

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        if(n==0):
            return 0
        begin,end = 0,0
        temp_sum = nums[begin]
        result = 0
        debug_tool = False
        while(begin<n and end<n):
            if(temp_sum < s):
                if(debug_tool):
                    print(begin,end,result,temp_sum,"A")
                if(end+1<n):
                    end += 1
                    temp_sum = temp_sum + nums[end]
                else:
                    break
            else:
                if(debug_tool):
                    print(begin,end,result,temp_sum,"B")
                if(result != 0):
                    result = min(result,end-begin+1)
                else:
                    result = end-begin+1
                temp_sum = temp_sum - nums[begin]
                begin += 1
                
        return result