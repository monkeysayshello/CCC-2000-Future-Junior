key = [x for x in input()]
y = input()
code = [x for x in y]
#print(code)
newcode = []
newkey = []
ans = []
finalans = []
for gh in code:
    #tmp = ord(chr)
    if gh.isalpha() == False:
        continue
    else:
        newcode.append(ord(gh))
for num in key:
    newkey.append(ord(num))
cnt = 0
#print(newkey,"newkey")
for thing in newcode:
    if cnt >= len(newkey):
        cnt = 0
    #print(cnt,newkey)
    #print(thing, "thing")
    measure = newkey[cnt]-65
    #print(measure,"measure",thing, "thing",cnt,"cnt")
    #print(measure,"measure")
    tmp = thing+measure
    if tmp > 90:
        tmp = tmp-90+64
    #print(tmp,"tmp")
    ans.append(tmp)
    cnt += 1
for x in ans:
    #print(x)
    g = chr(int(x))
    finalans.append(g)
OHMYGOD = "".join(finalans)
print(OHMYGOD)
#print(chr(84+19))
#print(chr(97))
#print(ord("Z"))
