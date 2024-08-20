<span style="color:green">简单</span>
<span style="color:red">困难</span>
<span style="color:orange">中等</span>



|题目|难度|解法|标签|经验|
|:--------|:-----------|:-----------|:---------------|:-------|
| <a href='https://leetcode.cn/problems/two-sum/?envType=study-plan-v2&envId=top-100-liked'> 1.两数之和</a> |<span style="color:green">简单</span>| 用map去实现快速查找；惰性建立map  |   哈希      |
| <a href='https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-100-liked'> 3. 无重复字符的最长子串</a> |<span style="color:orange">中等</span>| 先实现普通O(n2)的实现，然后分析题目，利用“上次失败地点”的信息，跳过一部分遍历;或者使用滑动窗口思想，遇到有重复时，右指针不动座指针一直挪动到两个指针之间没有重复时再开始挪动右指针  |   哈希，滑动窗口      |用滑动窗口思想，遇到有重复时，右指针不动左指针一直挪动到两个指针之间没有重复时再开始挪动右指针；要利用上次遍历时的失败信息
| <a href='https://leetcode.cn/problems/median-of-two-sorted-arrays/'> 4.找两个正序数组的中位数</a>|<span style="color:red">困难</span> | 实际上还是双指针,用两个指针来分隔左右的数据，需要利用上中位数的性质 | 双指针  | 中位数的性质：1左边最大小于右边最小 2:下标之和为(m+n+1)//2|
| <a href='https://leetcode.cn/problems/container-with-most-water/?envType=study-plan-v2&envId=top-100-liked'> 11. 盛最多水的容器</a> | <span style="color:orange">中等</span>|  一直移动矮边，就能快速找到   | 双指针   |  要找到移动矮边才有可能让容积增大的规律
| <a href='https://leetcode.cn/problems/3sum/description/'> 15.三数之和</a> |<span style="color:orange">中等</span>| 最差三层循环ijk，可以先排序数组，然后使用双指针找jk两数之和; 并且下一轮循环时检查是否和上一轮起点相同，进行去重  | 双指针   |为了保证答案不重复也方便按照值大小顺序查找，可以直接将数组排序      |
| <a href='https://leetcode.cn/problems/4sum/description/'> 18.四数之和</a> |<span style="color:orange">中等</span>| 最差四层循环ijkl，可以先排序数组，然后使用双指针找kl两数之和; 并且下一轮循环检查是否和上一轮起点相同，进行去重  | 双指针   |  三数之和换皮；注意ijk的下标有范围的，不用遍历到尾 |
| <a href='https://leetcode.cn/problems/trapping-rain-water/?envType=study-plan-v2&envId=top-100-liked'> 42. 接雨水</a> | <span style="color:red">困难</span>|  一直移动矮边,如果新移动的边比之前矮的还要矮就更新容积   | 双指针   | 和第11题那题一样的思路  要找到移动矮边才有可能让容积增大的规律
| <a href='https://leetcode.cn/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-100-liked'> 49. 字母异位词分组</a>|<span style="color:orange">中等</span>|  直接把出现的所有字符串进行排序，把排序后的字符当作键去搜构造字典    | 哈希   | 
| <a href='https://leetcode.cn/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-100-liked'> 128. 最长连续序列</a> | <span style="color:orange">中等</span>|  去重+排序，用一个变量记录最大的连续次数即可    | 哈希   |  查找时，可以直接对数组去重、排序
| <a href='https://leetcode.cn/problems/move-zeroes/description/?envType=study-plan-v2&envId=top-100-liked'> 283.移动零</a> | <span style="color:green">简单</span>|  N=0开始，遍历数组, 直接把非零数往前挪到第N位置，然后增大N。遍历结束以后把下标大于N的都设置为0   |  双指针  |  
| <a href='https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/?envType=study-plan-v2&envId=top-100-liked'> 438. 找到字符串中所有字母异位词 </a> | <span style="color:orange">中等</span>|  粗暴解法直接按固定步长便历，然后比较子串是否相等（但是比较要用技巧）    |  滑动窗口，哈希  | 异位词比较是否相等：被比较的串可以先排序，比较的时候都先把字符串排序再比较相等（python解法不超时但是性能落后）； **可以用哈希数组（利用全小写字母的特点，直接建立一个26维的数组），用这种方式进行比较是否相等**



