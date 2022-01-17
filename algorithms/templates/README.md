

### 存放模板代码的地方。


#### 滑动窗口//虫取

```python
def findSubArray(nums):
    N = len(nums) # 数组/字符串长度
    left, right = 0, 0 # 双指针，表示当前遍历的区间[left, right]，闭区间
    sums = 0 # 用于统计 子数组/子区间 是否有效，根据题目可能会改成求和/计数
    res = 0 # 保存最大的满足题目要求的 子数组/子串 长度
    while right < N: # 当右边的指针没有搜索到 数组/字符串 的结尾
        sums += nums[right] # 增加当前右边指针的数字/字符的求和/计数
        while 区间[left, right]不符合题意：# 此时需要一直移动左指针，直至找到一个符合题意的区间
            sums -= nums[left] # 移动左指针前需要从counter中减少left位置字符的求和/计数
            left += 1 # 真正的移动左指针，注意不能跟上面一行代码写反
        # 到 while 结束时，我们找到了一个符合题意要求的 子数组/子串
        res = max(res, right - left + 1) # 需要更新结果
        right += 1 # 移动右指针，去探索新的区间
    return res

```


#### 回溯模板

```python
def backtrack(path, state, opts):
    if base:  # 基线条件
        res.append(path)
        return
    for opt in opts:
        if prune:  # 剪枝条件
            continue/break
        # 保存现场（做出选择）
        path.append(opt)
        state = change(state)
        opts.remove(opt)
        # 递归
        backtrack(path, state, opts)
        # 恢复现场（撤销选择）
        path.remove(opt)
        state = unchange(state)
        opts.append(opt)

```

什么是回溯法\

回溯法（探索与回溯法）是一种选优搜索法，又称为试探法，按选优条件向前搜索，以达到目标。但当探索到某一步时，发现原先选择并不优或达不到目标，就退回一步重新选择，这种走不通就退回再走的技术为回溯法，而满足回溯条件的某个状态的点称为“回溯点”。

无重复元素全排列问题

给定一个所有元素都不同的list，要求返回list元素的全排列。

设n = len(list)，那么这个问题可以考虑为n叉树，对这个树进行dfs，这个问题里的回溯点就是深度（也就是templist的长度）为n时，回溯的条件就是当前元素已经出现在templist中了。

https://blog.csdn.net/PKU_Jade/article/details/78020794

