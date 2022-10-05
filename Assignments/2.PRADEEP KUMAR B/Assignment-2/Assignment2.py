import random

t = random.randint(0,100)
h = random.randint(0,100)

print("Temperature is = ",t)
print("Humidity is = ",h)

if t >60 and h > 60:
    print("alarm ON : It is to be risky")
elif t > 60 and h < 60:
    print("alarm ON : It is to be high temperature")
else:
    print("alarm OFF")
