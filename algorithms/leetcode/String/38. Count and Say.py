'''
38. Count and Say
Easy

994

7870

Add to List

Share
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.



Example 1:

Input: 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", so the answer is the concatenation of "12" and "11" which is "1211".
'''
class Solution:
    def countAndSay(self, n: int) :
        if n == 1:
            return "1"
        if n == 2:
            return "11"

        res = 11
        for i in range(2, n):
            res = self.count_one_number(str(res))
        return res
    def count_one_number(self,string):
        #J聚合一个
        l = string[0]
        res = ""
        temp  = string[0]
        for i in range(1,len(string)):
            if string[i]== string[i-1]:
                temp+=string[i]
            elif string[i] != string[i-1]:
                # res.append([temp,len(temp)])
                res+=str(len(temp))+temp[0]
                temp = string[i]
            if i == len(string)-1:
                res += str(len(temp)) + temp[0]

        return res





if __name__ == '__main__':
    sc =Solution()
    print(sc.count_one_number(str(1211)))
    print(sc.countAndSay(5))