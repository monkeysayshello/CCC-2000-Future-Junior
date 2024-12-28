day = int(input())
evening = int(input())
weekend = int(input())
daya = (day-100)*0.25
if daya < 0:
    daya = 0
theresta = (evening*0.15)+(weekend*0.2)
dayb = (day-250)*0.45
if dayb < 0:
    dayb = 0
therestb = (evening*0.35)+(weekend*0.25)
suma = round(daya+theresta,2)
sumb = round(dayb+therestb,2)
txta = "Plan A costs {tmp:.2f}"
txtb = "Plan B costs {tmp:.2f}"
print(txta.format(tmp=suma))
print(txtb.format(tmp=sumb))
if suma < sumb:
    print("Plan A is cheapest.")
elif suma == sumb:
    print("Plan A and B are the same price.")
else:
    print("Plan B is cheapest.")
#print(suma,sumb)
