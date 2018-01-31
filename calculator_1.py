#!/usr/bin/env python3

import sys

try:

    IdandPaydict = {}
    for IdandPay in sys.argv[1:]:
        Id_Pay = IdandPay.split(':')
        IdandPaydict[Id_Pay[0]] = float(Id_Pay[1])

except:

    print("Parameter Error")
    exit() 

def calculator_1(number):

    number = number * (1 - 0.08 - 0.02 - 0.005 - 0.06)
    number = number - 3500
    if number <= 0:
        tax = 0

    elif number <= 1500:
        tax = number * 0.03

    elif number <= 4500:
        tax = number * 0.10 - 105

    elif number <= 9000:
        tax = number * 0.20 - 555

    elif number <= 35000:
        tax = number * 0.25 - 1005

    elif number <= 55000:
        tax = number * 0.30 - 2755

    elif number <= 80000:
        tax = number * 0.35 - 5505

    else:
        tax = number * 0.45 - 13505
    return tax

for Id,Pay in IdandPaydict.items():
    tax = (calculator_1(float(Pay)))
    salary = Pay*(1-0.08-0.02-0.005-0.06) - tax
    print ("%s:%.2f" %(Id,salary))

