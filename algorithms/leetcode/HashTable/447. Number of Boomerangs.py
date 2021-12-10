'''
447. Number of Boomerangs
You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Return the number of boomerangs.

 

Example 1:

Input: points = [[0,0],[1,0],[2,0]]
Output: 2
Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].
Example 2:

Input: points = [[1,1],[2,2],[3,3]]
Output: 2
Example 3:

Input: points = [[1,1]]
Output: 0
 

Constraints:

n == points.length
1 <= n <= 500
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
'''
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        if len(points) < 3:return 0 
        # 对于点i 算所有点离其距离 每一个距离都是其频数 m *(m-1) 即
        for i in range(len(points)):
            map = {}
            for j in range(len(points)):
                if i!= j:
                    a = points[i]
                    b = points[j]
                    dist = (a[0] - b[0])*(a[0] - b[0])+(a[1] - b[1])*(a[1] - b[1])
                    if dist not in map:
                        map[dist] = 1
                    else:
                        map[dist] += 1
            for m in map.values():
                res += m * (m - 1)
        return res

if __name__ == '__main__':
    so = Solution()
    print(so.numberOfBoomerangs([[0,0],[1,0],[2,0]]))