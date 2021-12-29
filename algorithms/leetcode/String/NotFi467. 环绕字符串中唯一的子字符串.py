'''
467. 环绕字符串中唯一的子字符串
We define the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this:

"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
Given a string p, return the number of unique non-empty substrings of p are present in s.

 

Example 1:

Input: p = "a"
Output: 1
Explanation: Only the substring "a" of p is in s.
Example 2:

Input: p = "cac"
Output: 2
Explanation: There are two substrings ("a", "c") of p in s.
Example 3:

Input: p = "zab"
Output: 6
Explanation: There are six substrings ("z", "a", "b", "za", "ab", and "zab") of p in s.
 

Constraints:

1 <= p.length <= 105
p consists of lowercase English letters.
通过次数9,523提交次数21,522

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-substrings-in-wraparound-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int: