class Solution:
    def maxValue(self, nums):
        n = len(nums)
        
        suf_min = [0] * n
        suf_min[-1] = nums[-1]
        
        for i in range(n - 2, -1, -1):
            suf_min[i] = min(nums[i], suf_min[i + 1])
        
        ans = [0] * n
        
        start = 0
        pref_max = nums[0]
        seg_max = nums[0]
        
        for i in range(n - 1):
            pref_max = max(pref_max, nums[i])
            seg_max = max(seg_max, nums[i])
            
            if pref_max <= suf_min[i + 1]:
                for j in range(start, i + 1):
                    ans[j] = seg_max
                
                start = i + 1
                pref_max = nums[start]
                seg_max = nums[start]
        
        seg_max = max(nums[start:])
        for j in range(start, n):
            ans[j] = seg_max
        
        return ans