class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        mymax = 0
        i = 0
        j = len(height)-1
        while i < j:
            area = abs(i - j) * min(height[i], height[j])
            mymax = max(area, mymax)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
                
        return mymax

s = Solution()
#print(s.maxArea([1,1,2,3,4,5,1,1]))
#assert s.maxArea([1,1,2,3,4,5,1,1]) == 1
#assert s.maxArea([1,1]) == 1
assert s.maxArea([1,2]) == 1
