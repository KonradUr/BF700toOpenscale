#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 11:34:53 2021

based on:
https://github.com/giuaig/sanitas2openscale

adapted by: Konrad Urbański

Convert Beuer BF700 csv file that openScale can import.
Tested with openScale v2.3.5-pro and Beuer data exported from beuer-connect www (January 2021).
.
usage:
    python3 bf2osc.py my_beuer_file.csv my_file_openscale.csv
"""

import sys
import os
import csv

plik=str(sys.argv[1])
plik2=str(sys.argv[2])

if os.path.isfile(plik):
    pass
else:
    print("File not found!")
    sys.exit(1)


#%%

dane=[]
with open(plik, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    rr=-1
    for row in reader:
        rr+=1
        if rr>=17: #start row with data
            ss=-1
            col=[]
            for e in row:
                ss+=1
                col.append(e)

            dane.append(col)


#%%

with open(plik2, 'w', newline='') as csvfile:
    fieldnames = ["biceps","bone","caliper1","caliper2","caliper3","calories","chest","comment","dateTime","fat","hip","lbm","muscle","neck","thigh","visceralFat","waist","water","weight"]

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()


    for wiersz in range(0,len(dane)-1):
        dataczas=dane[wiersz][0][7:11]+'-'+dane[wiersz][0][4:6]+'-'+dane[wiersz][0][1:3]+' '+dane[wiersz][1][1:6]
        writer.writerow({"biceps": 0.0, "bone": float(dane[wiersz][7]), "caliper1": 0.0, "caliper2": 0.0, "caliper3": 0.0, "calories": 0.0, "chest": 0.0, "comment": dane[wiersz][9][1:-1], "dateTime": dataczas, "fat": float(dane[wiersz][4]), "hip": 0.0, "lbm": 0.0, "muscle": float(dane[wiersz][6]), "neck": 0.0, "thigh": 0.0, "visceralFat": 0.0, "waist": 0.0, "water": float(dane[wiersz][5]), "weight": float(dane[wiersz][2])})

