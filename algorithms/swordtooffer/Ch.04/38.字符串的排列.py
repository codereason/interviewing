def prem(str):
    if len(str)==0:
        return ""
    dfs(str,str)

def dfs(str):
    for char in str:
