class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) == 0 and len(nums2) == 1:
            return nums2[0]
        elif len(nums1) == 1 and len(nums2) == 0:
            return nums1[0]
        elif len(nums2) == 0:
            nums2.append(nums1.pop())
        elif len(nums1) == 0:
            nums1.append(nums2.pop())

        if len(nums1) == 1 and len(nums2) == 1:
            return(nums1[0]+nums2[0])/2

        totallength = len(nums1) + len(nums2)

        i1 = 0
        i2 = 0
        midpoint = totallength / 2
        self.mids = []
        
        for i in range(0, int(midpoint) + 1):
            if i1 >= len(nums1):
                self.mids.append(nums2[i2])
                i2 += 1
                continue
            elif i2 >= len(nums2):
                self.mids.append(nums1[i1])
                i1 += 1
                continue
            if nums1[i1] < nums2[i2]:
                self.mids.append(nums1[i1])
                i1 += 1
            else:
                self.mids.append(nums2[i2])
                i2 += 1

        if totallength % 2 == 0:
            return (self.mids[-1]+self.mids[-2])/2
        else:
            if len(self.mids) < 2:
                return self.mids[0]
            return self.mids[-1]

s = Solution()
assert s.findMedianSortedArrays([1, 2, 3, 4], [5]) == 3.0
assert s.findMedianSortedArrays([2], [2]) == 2
assert s.findMedianSortedArrays([1, 2], [3]) == 2
assert s.findMedianSortedArrays([2, 2], [10]) == 2
assert s.findMedianSortedArrays([1, 3], [2]) == 2
assert s.findMedianSortedArrays([1, 3, 5], [2, 4, 6]) == 3.5
assert s.findMedianSortedArrays([], [1]) == 1
assert s.findMedianSortedArrays([2], []) == 2
assert s.findMedianSortedArrays([2, 3], []) == 2.5
assert s.findMedianSortedArrays([], [4, 5]) == 4.5
assert s.findMedianSortedArrays([2], [3]) == 2.5
assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5

#Fastest python3 solution on leetcode as of mar2018
