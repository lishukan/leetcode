from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        results = [-1] * len(s)
        last_pos = -1
        for index,i in enumerate(s):
            if i==c:
                if last_pos==-1:
                    for k in range(index):
                        results[k]=index-k

                else:
                    mid = (index+last_pos)//2
                    if  last_pos<mid<index:
                        for j in range(last_pos+1,mid+1):
                            results[j]=j-last_pos
                        for j in range(mid+1,index):
                            results[j] = index-j
                    
                last_pos =index
                results[index]=0

        for j in range(last_pos,len(s)):
            if results[j]==-1:
                results[j]=j-last_pos

        return results


if __name__ == '__main__':
    s = "loveleetcode"
    c = "e"
    #[3,2,1,0,1,0,0,1,2,2,1,0]
    print(Solution().shortestToChar(s,c))
    s = "baab"
    c = "b"
    #[3,2,1,0,1,0,0,1,2,2,1,0]
    print(Solution().shortestToChar(s,c))