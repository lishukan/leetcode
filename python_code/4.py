class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #确保nums1是最短
        m,n = len(nums1),len(nums2)
        if m>n:
            nums1,nums2,m,n = nums2,nums1,n,m
        if m==0:
            if n%2==1:
                return nums2[n//2]
            else:
                return (nums2[n//2]+nums2[n//2-1])/2
        # 中位数满足的条件
        # 1. 左边的数都小于右边的数
        # 2. 左边的数的个数等于右边的数的个数
        target_sum = (m+n+1)//2
        index_1=0
        while index_1<=m:
            index_2=target_sum-index_1
            if index_1==0:
                left_max = nums2[index_2-1]
                if index_2 == n:
                    #      |123  
                    #   345| 
                    right_min = nums1[index_1]
                else:
                    #       |123
                    #   4567|8     
                    right_min = min([nums1[index_1],nums2[index_2]])

            elif index_1==m:
                #    123|
                #       |456
                right_min = nums2[index_2]
                if index_2==0:
                    left_max = nums1[index_1-1]
                else:
                    #   123|
                    #     4|567
                    left_max = max([nums1[index_1-1],nums2[index_2-1]])                    
            else:
                left_max = max([nums1[index_1-1],nums2[index_2-1]])
                right_min = min([nums1[index_1],nums2[index_2]])
            if left_max<=right_min:
                break
            index_1+=1
        if (m+n)%2==1:
            return left_max
        else:
            return (left_max+right_min)/2