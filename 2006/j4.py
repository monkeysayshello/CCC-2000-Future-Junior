import copy
directions = {1:[2],2:[],3:[],4:[1,3],5:[3],6:[],7:[1]}
#input = []
while True:
    tmp = []
    for i in range(2):
        n = int(input())
        tmp.append(n)
    if tmp[0] == 0 and tmp[1] == 0:
        break
    else:
        directions[tmp[1]].append(tmp[0])
ans = []
remove = "Nothing"
lastdirections = "Nothing"
impossible = False
while len(ans) != 7:
    for key in directions:
        if len(directions[key]) == 0:
            ans.append(key)
            directions[key] = ["Clear"]
            remove = key
            break
    for key in directions:
        if remove in directions[key]:
            directions[key].remove(remove)
    if lastdirections == directions:
        impossible = True
        break
    else:
        lastdirections = copy.deepcopy(directions)
    #print(directions)
if impossible == True:
    print("Cannot complete these tasks. Going to bed.")
else:
    print(*ans)#directions)
