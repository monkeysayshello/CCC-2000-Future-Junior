x = int(input())
y = int(input())
txt = "All positions change in year {price}"
print(txt.format(price=x))
tmp = 0
tmp += x
while True:
    tmp += 60
    
    if tmp <= y:
        print(txt.format(price=tmp))
    else:
        break
