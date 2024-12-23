n = int(input())
up = int((n-1)/2)
cnt = 1
middle = (n*2)-2
for i in range(up):
    print("*"*cnt+" "*middle+"*"*cnt)
    cnt += 2
    middle -= 4
#print(cnt,middle)
cnt -= 2
middle += 4
tmp = (cnt*2)+middle
#print(cnt,middle)
print("*"*(tmp))
for i in range(up):
    print("*"*cnt+" "*middle+"*"*cnt)
    cnt -= 2
    middle += 4
