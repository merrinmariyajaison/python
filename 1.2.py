print("Enter the units consumed")
units=int(input())
if units <=200:
    bill=units*0.50
elif units >=201 and units<=401:
    bill=units*0.65
elif units >=401 and units>=600:
    bill=units*0.80
else:
    bill=units*1
    
if bill<100:
    bill=100
    
if bill>400:
    bill=bill*0.15+bill
print("bill ",bill)