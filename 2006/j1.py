ans = 0
burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())
if burger == 1:
    ans += 461
elif burger == 2:
    ans += 431
elif burger == 3:
    ans += 420

if side == 1:
    ans += 100
elif side == 2:
    ans += 57
elif side == 3:
    ans += 70

if drink == 1:
    ans += 130
elif drink == 2:
    ans += 160
elif drink == 3:
    ans += 118
if dessert == 1:
    ans += 167
elif dessert == 2:
    ans += 266
elif dessert == 3:
    ans += 75
txt = "Your total Calorie count is {dude}."
print(txt.format(dude=ans))
