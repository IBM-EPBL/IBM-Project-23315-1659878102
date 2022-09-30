import random as r
temperature=r.randrange(30,130)
humudity=r.randrange(40,150)
print(temperature,humudity)
if temperature>100:
    if humudity>80:
        print("DANGEROUS")
    else:
        print("HIGH TEMPERATURE")
elif temperature==100:
    print("No risk")
else:
    print("Good")
