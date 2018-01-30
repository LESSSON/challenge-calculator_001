#!/usr/bin/env python3

import sys

try:

    number = int(sys.argv[1])
    if len(sys.argv) > 2:
        raise ValueError()

except ValueError:

    print("Parameter Error")
    exit() 

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

print("%.2f"%tax)
