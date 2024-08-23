from typing import List

class Solution:


    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        注意要求是连续的数组

        我们假设 nums = [1,2,1,2,1] ,k=3 
        我们的前缀和数组为
        [1,3,4,6,7]   这里只能拿到 从0到i的和
        如果想要拿到从i到j的和，我们需要把数组进行更新，减去前面的和
        即 构建 N维数组
        [1,3,4,6,7] 
        [0,2,3,5,6]
        [0,0,1,3,4]
        [0,0,0,2,3]
        [0,0,0,0,1]
        这样我们直接便利这个数组看其中有多少个值为k的即可
        但是这样的空间复杂度是O(n^2)时间复杂度是O(n^2)，顶多我们可以优化到O(n)的空间复杂度，只用一个数组，但是时间复杂度还是O(n^2)
        优化： 我们使用一个字典来存储前缀和的个数，
        假设  pre[0-i]，i>j 是 从0到i的前缀和，那么 pre[0-j] = pre[0-i] - pre[j-i]
        假设此时我们计算出 pre[0~i]= x,  我们想知道此时有多少个 pre[j~i]=k  等同于求多少 pre[0~j-1] = x-k
        因为  pre[0~j-1]+ pre[j~i]=pre[0~i]  即    x-k   +  k = x 
        a b c d e f g h i j k l m n o p q r s t u v w x y z
        --------------------- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            pre[0~j-1] ==x-k?          pre[j~i]   ==k (if pre[0~i] ==x-k)
              ============================
                    pre[0~i] =x
         
        此时 pre[0~j-1] 我们早就计算过了，可以直接查找
        因此我们可以建立一个字典，存储前缀和的个数，当我们计算到某个前缀和时，我们可以直接查找有多少个前缀和等于 x-k
        """ 
        count=0
        # 用来存储前缀和的个数
        appear_dict={0:1} # 前缀和为0的个数设为1（说实话这里我看不太懂，我理解这里是  相当于  pre[0~i] 直接等于k 的情况   ）
        presum = 0
        for i in nums:
            presum = presum +i
            count+=appear_dict.get(presum-k,0)
            appear_dict[presum] = appear_dict.get(presum,0)+1
        return count





if __name__ == '__main__':
    print(Solution().subarraySum([1,1,1],2)) 
    print(Solution().subarraySum([1,2,3],3))
    print(Solution().subarraySum([1,2,1,2,1],3))
    print(Solution().subarraySum([1,2,3,4,5,6,7,1,23,21,3,1,2,1,1,1,1,1,12,2,3,2,3,2,2],1))