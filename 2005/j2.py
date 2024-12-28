def check(n):
    amt = 2
    cnt = 2
    while cnt < n:
        if amt > 4:
            return False
            break
        if n % cnt == 0:
            amt += 1
        cnt += 1
    if amt == 4:
        return True
    else:
        return False
x = int(input())
y = int(input())
ans = 0
for i in range(x,y+1):
    if check(i):
        ans += 1
txt = "The number of RSA numbers between {x} and {y} is {ans}"
print(txt.format(x=x,y=y,ans=ans))
