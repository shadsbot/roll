#!/usr/bin/env python

import sys
import re
from random import randint

for arg in sys.argv:
        if "/" in arg:
                pass
        elif arg == "roll.py":
                pass
        else:
                string = arg.split("d")
                amount = re.split('([-+]\d*)', string[1])
                dice = amount[0]
                number = int(string[0]);
                print("Rolling %s..." % arg)
                arr = []
                for x in range(0,number):
                        num = randint(1,int(dice))
                        arr.append(num)
                        print(num)
                if len(arr) > 1:
                        print("Total is %s" % sum(arr))
                if len(amount) > 1:
                        modifyer = amount[1]
                        print("Modified Total is %s" % (sum(arr) + int(modifyer)))
                print("")
                print("")
