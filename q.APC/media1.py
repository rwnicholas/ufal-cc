#!/usr/bin/python3

cd = float(input())
aliquota = float(input())
vprod = float(input())
vfrete = float(input())
vprod = vprod*cd
vfrete = vfrete*cd
aliquota = aliquota/100
vimporta = round(vprod*0.6)
if vprod/cd>2500:
    vfinal = (vprod+vimporta/(1-aliquota))
else:
    vfinal = (vprod+vfrete+vimporta)/(1-aliquota)

icms = round(vfinal*aliquota,2)
print('vfinal', vfinal)
print(cd)
print(vprod)
print(vfrete)
print(vfrete+vprod)
print(vprod*0.6)
print(icms)
print(round((vprod*0.6)+icms,2))
print(round(vfinal+icms,2))