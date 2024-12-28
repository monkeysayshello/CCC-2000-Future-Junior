x = int(input())
import math
def check(n):
    tmp1 = math.sqrt(n)
    tmp2 = round(tmp1,0)
    if tmp1 == tmp2:
        return True
    else:
        return False
while True:
    if check(x):
        tmp = int(math.sqrt(x)) 
        g = "The largest square has side length {price}." 
        print(g.format(price=tmp))
        break
    else:
        x -= 1
