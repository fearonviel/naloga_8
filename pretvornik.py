#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("Dobrodošli. Ta program pretvori kilometre v milje.")

while True:
    vneseni_km = float(raw_input("Vnesite število kilometrov: "))
    milje = vneseni_km * 0.621371
    print(str(vneseni_km) + " km je " + str(milje) + " milj(e).")

    nov_vnos = raw_input("Želite pretvoriti novo število kilometrov? (Da/ne): ").lower()

    if nov_vnos == "ne":
        break

print("END")