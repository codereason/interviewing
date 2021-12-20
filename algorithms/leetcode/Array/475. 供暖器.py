'''
475. 供暖器
冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。

在加热器的加热半径范围内的每个房屋都可以获得供暖。

现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。

说明：所有供暖器都遵循你的半径标准，加热的半径也一样。

 

示例 1:

输入: houses = [1,2,3], heaters = [2]
输出: 1
解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
示例 2:

输入: houses = [1,2,3,4], heaters = [1,4]
输出: 1
解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
示例 3：

输入：houses = [1,5], heaters = [2]
输出：3
 

提示：

1 <= houses.length, heaters.length <= 3 * 104
1 <= houses[i], heaters[i] <= 109
'''
class Solution:
    def findRadius__TLE(self, houses, heaters):
         
        res = 0
        radius = 0
        
        while radius<=100000:
            tmp = set()  ##能辐射到的房子

            for i in range(radius):
                for heat in heaters:
                    if heat - i in houses:
                        tmp.add(heat-i)
                    if heat + i in houses:
                        tmp.add(heat+i)
                if set(houses) in tmp or set(houses) == tmp:
                    res = i
                    break

            
            radius+=1
        return res

if __name__ == "__main__":
    so = Solution()
    houses =  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    heaters = [2]

    print(so.findRadius(houses,heaters))