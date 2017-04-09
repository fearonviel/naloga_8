#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("Dobrodošli.")

x = 0
vneseno_stevilo = int(raw_input("Vnesite število med 1 in 100: "))

while x < vneseno_stevilo:

    x = x + 1

    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
        continue

    elif x % 3 == 0:
        print("fizz")
        continue

    elif x % 5 == 0:
        print("buzz")
        continue

    print(x)

print("END")

