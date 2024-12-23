x = int(input())
m = int(input())
ans = 0
for i in range(1,m):
    tmp = int(round((x*i/m),0))
    subans = (x*i)-(m*tmp)
    #print(tmp,i,x,m)
    if subans == 1 and i > ans:
        ans = i
    #if tmp > 1:
    #    break
if ans == 0:
    print("No such integer exists.")
else:
    print(ans)
