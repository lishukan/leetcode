from typing import List

class Solution:

    
    def trap(self, height: List[int]) -> int:
        """
        先确定左边和右边的谁高谁低，然后移动矮边，
        移动以后如果矮子比之前的矮子高，那么就更新矮子的高度，如果矮子比之前的矮子低，那么就计算面积。

        2 0 3 1 5 5 1 ->  2 0 3 1 5 5  are=0,->  0 3 1 5 5  are=2,->  3 1 5 5  are=2, ->  1 5 5  are=4,->  5 5  are=4
        """
        left, right = 0, len(height)-1
        low_pre = 0
        area = 0
        while left<right:
            if height[left]<=low_pre:
                #移动以后 左边的高度比之前矮子低
                area += low_pre - height[left]
                left+=1
                continue
            else:
                # 移动以后 左边的高度比之前的矮子高
                if height[left]<=height[right]:
                    low_pre = height[left]
                    left+=1
                else:
                    # 移动以后 左边的高度比右边的高度高 且 右边的高度比之前的矮子低
                    if height[right]<=low_pre:
                        area += low_pre - height[right]
                        right-=1
                        continue
                    else:
                        # 移动以后 左边的高度比右边的高度高 且 右边的高度比之前的矮子高
                        low_pre = height[right]
                        right-=1
        return area
            

if __name__ == '__main__':
    print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])) #6
    print(Solution().trap([4,2,0,3,2,5])) #9
    print(Solution().trap([4,2,3])) #1
    print(Solution().trap([4,2,3,1])) #1
    print(Solution().trap([4,2,3,1,2])) #2
    print(Solution().trap([4,2,3,1,2,1])) #2
    print(Solution().trap([4,2,3,1,2,1,3])) #6
    print(Solution().trap([4,2,3,1,2,1,3,1])) #6
    print(Solution().trap([4,2,3,1,2,1,3,1,2])) #7
    print(Solution().trap([4,2,3,1,2,1,3,1,2,1])) #7
    print(Solution().trap([2,0,3,1,5,5,1])) #8




