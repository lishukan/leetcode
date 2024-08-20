class Solution:


    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if len(s)<=1:
    #         return len(s)
    #     max_length,last_fail,dup_set= 1,0,{s[0]}
    #     for idx in range(0, len(s)-1):
    #            
    #         dup_set = {s[i] for i in range(idx, last_fail)}
    #         # print("初始化",dup_set,idx,last_fail)
    #         for j in range(last_fail, len(s)):
    #             # print(dup_set)
    #             if s[j] not in dup_set:
    #                 dup_set.add(s[j])
    #             else:
                     # 记录下此时失败的位置
    #                 last_fail=j
    #                 if len(dup_set)>max_length:
    #                     max_length=len(dup_set)
    #                 break
    #         if len(dup_set)>max_length:
    #             max_length=len(dup_set)
        
    #     return max_length

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        if len(s)==2:
            return 2 if s[0]!=s[1] else 1
        
        right_idx,max_length = -1,0
        dup_set =set()
        for i in range(len(s)):
            if i!=0:
                #
                dup_set.remove(s[i-1])

            while right_idx+1<len(s) and s[right_idx+1] not in dup_set:
                dup_set.add(s[right_idx+1])
                right_idx+=1

            if right_idx+1-i>max_length:
                max_length = right_idx+1-i
        return max_length

    # 以下是官方题解
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     # 哈希集合，记录每个字符是否出现过
    #     occ = set()
    #     n = len(s)
    #     # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
    #     rk, ans = -1, 0
    #     for i in range(n):
    #         if i != 0:
    #             # 左指针向右移动一格，移除一个字符
    #             occ.remove(s[i - 1])
    #         while rk + 1 < n and s[rk + 1] not in occ:
    #             # 不断地移动右指针
    #             occ.add(s[rk + 1])
    #             rk += 1
    #         # 第 i 到 rk 个字符是一个极长的无重复字符子串
    #         ans = max(ans, rk - i + 1)
    #     return ans



if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("bbbbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
    print(Solution().lengthOfLongestSubstring("au"))
    print(Solution().lengthOfLongestSubstring("cdd"))
    print(Solution().lengthOfLongestSubstring("jbpnbwwd"))
    print(Solution().lengthOfLongestSubstring("dvdf"))