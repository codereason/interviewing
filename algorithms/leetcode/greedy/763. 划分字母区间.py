'''
763. 划分字母区间
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

 

示例：

输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
 

提示：

S的长度在[1, 500]之间。
S只包含小写字母 'a' 到 'z' 。
通过次数89,140提交次数116,828
'''
'''
说明一下边界问题：已经知道某个字母的最右侧边界 例如：a为8
当我们遍历a对应的区间[0,8]将会出现b，c等字母，假设 b 的右侧边界为 5 因为5小于初始a的8 那么b符合条件(取a[0,8])
但是当c 假设为11 那么我们遍历到c时 如果取[0,8]必然不对了，那么这个片段的边界就该更新为11了，end变为11，这个时候继续
遍历，不断判断边界，大了就跟新边界。最终当我们的遍历的索引等于边界索引，意味着这个区间内不存在字母的最右侧索引大于现在
的边界，这个时候，一个片段的截止位置就找到了，而我们的起始位置是0，第一个便找到了。然后更新起始位置索引继续获取就可以了。
'''


class Solution:
    def partitionLabels(self, s: str) :
        map = {}
        res = []
        for i in range(len(s)):
            map[s[i]] = i 
        l, r = 0, 0 
        for i in range(len(s)):
            r = max(map[s[i]] , r)
            if i == r: # find the boundary then segment
                res.append(r-l+1)
                l = r+1
        return res
if __name__ == '__main__':
    so = Solution()
    string = "ababcbacadefegdehijhklij"
    print(so.partitionLabels(string))