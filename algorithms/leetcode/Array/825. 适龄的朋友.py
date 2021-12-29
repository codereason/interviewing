'''
在社交媒体网站上有 n 个用户。给你一个整数数组 ages ，其中 ages[i] 是第 i 个用户的年龄。

如果下述任意一个条件为真，那么用户 x 将不会向用户 y（x != y）发送好友请求：

age[y] <= 0.5 * age[x] + 7
age[y] > age[x]
age[y] > 100 && age[x] < 100
否则，x 将会向 y 发送一条好友请求。

注意，如果 x 向 y 发送一条好友请求，y 不必也向 x 发送一条好友请求。另外，用户不会向自己发送好友请求。

返回在该社交媒体网站上产生的好友请求总数。

 

示例 1：

输入：ages = [16,16]
输出：2
解释：2 人互发好友请求。
示例 2：

输入：ages = [16,17,18]
输出：2
解释：产生的好友请求为 17 -> 16 ，18 -> 17 。
示例 3：

输入：ages = [20,30,100,110,120]
输出：3
解释：产生的好友请求为 110 -> 100 ，120 -> 110 ，120 -> 100 。
 

提示：

n == ages.length
1 <= n <= 2 * 104
1 <= ages[i] <= 120
通过次数10,312提交次数24,439

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/friends-of-appropriate-ages
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

拆解
'''

class Solution:
    def numFriendRequests__TLE(self, ages):
        res = 0
        ages.sort()
        for i in range(len(ages)):
            j = i+1 
            while j < len(ages):
                if not ( ages[i] <= 0.5 * ages[j] + 7 or ages[i] > ages[j] or (ages[i] > 100 and ages[j] < 100)):
                    res +=1
                    if ages[j] == ages[i]:
                        res += 1 
                
                j+=1 
        
        return res

'''
ages[i] > 0.5 * ages[j] + 7 and  ages[i] <= ages[j]  维护边界+双指针  答案来自官方
'''
class Solution2:
    def numFriendRequests(self, ages) -> int:
        n = len(ages)
        ages.sort()
        left = right = ans = 0
        for age in ages:
            if age < 15:
                continue
            while ages[left] <= 0.5 * age + 7:
                left += 1
            while right + 1 < n and ages[right + 1] <= age:
                right += 1
            ans += right - left
        return ans

# class Solution3:
#     def numFriendRequests(self, ages) -> int:
#         n = len(ages)
#         list = 120 * [0]
#         ages.sort()
#         for age in ages:
#             if age < 15:
#                 continue
#             list[age-1]+=1 
#         return ans


if __name__ == "__main__":
    solu = Solution2()
    ages = [73,106,39,6,26,15,30,100,71,35,46,112,6,60,110]
    print(solu.numFriendRequests(ages))