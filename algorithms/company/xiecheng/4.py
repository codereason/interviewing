wordDict= list(map(str,input().split(",")))
sentence = str(input())
Flag = False
q = [sentence]
already_seen = set()

while len(q) > 0:
    curr_s = q.pop(0)
    
    if curr_s not in already_seen:
        already_seen.add(curr_s)
        if curr_s == '':
            Flag = True
            
        for w in wordDict:
            if curr_s.startswith(w):
                q.append(curr_s[len(w):])

print("YES") if Flag ==True else print("NO")
    
# 我,要,爱,携程,携程旅行网
# 我爱携程旅行网
