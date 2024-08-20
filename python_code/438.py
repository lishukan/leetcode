from typing import List

class Solution:
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     p = sorted(p)
    #     results= []
    #     for i in range(0,len(s)-len(p)+1):
    #         if self.is_valid(s[i:i+len(p)],p):
    #             results.append(i)
    #     return results

    # def is_valid(self, a, b):
    #     """
    #     判断a，b是不是 异位词
    #     这里假设b已经排序过
    #     """
    #     return sorted(a) == b

    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_map, p_map = [0]*26, [0]*26
        if len(p) > len(s):
            return []
        for i in range(0, len(p)):
            p_map[ord(p[i])-97] += 1
            s_map[ord(s[i])-97] += 1
        results=[]
        if s_map==p_map:
            results.append(0)
        
        for i in range(len(s)-len(p)):
            s_map[ord(s[i])-97]-=1
            s_map[ord(s[i+len(p)])-97]+=1

            if s_map==p_map:
                results.append(i+1)
        
        return results
        


if __name__ == '__main__':
    print(Solution().findAnagrams("cbaebabacd","abc"))
    print(Solution().findAnagrams("abab","ab"))