# -*- coding: utf-8 -*-
"""Assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_D-LYr0s9SNBtW8eG5piNLJUs0zzKT3S
"""

import random

t=random.randint(1,150)
h=random.randint(1,150)

if t>75:
    if h>75:
        print("hazard predected ,temperature: {t1} Humidity: {h1}".format(t1=t,h1=h))
        print("Alarm ON")
    else:
        print("high temperature , temperature:",t )
        print("Alarm ON")
else:
    print("all good ,temperature: {t1} Humidity: {h1}".format(t1=t,h1=h))
    print("Alarm OFF")