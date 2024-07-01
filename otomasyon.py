#DETAY DOSYA DUZENLEYICI
from datetime import datetime
import os

pathforSettings = 'ayarlar.txt'
isAyarlar = os.path.isfile(pathforSettings)

now = datetime.now()
day = now.day
month = now.month
year = now.year

if(isAyarlar):
    ayarlar = open(pathforSettings, 'r')
    lines = ayarlar.readlines()
    parent_dir = lines[1].strip()

    grapherCount = int(lines[3].strip())
    graphers = []

    for x in range(grapherCount):
        graphers.append(lines[x + 5].strip())

    ayarlar.close()


    for y in range(grapherCount):
        for x in range(3):
            os.makedirs(os.path.join(parent_dir, "DAILY", f"{month}", f"{day}.{month}.{year}", graphers[y] , str(x)))

    SIDEPHOTOS = ["A LA CARTE", "AMPHITHEATRE", "BAR", "SUNSET", "POOL", "SLIDES", "BEACH", "WATER SPORTS", "ROAD"]
    for z in range(9):
        os.makedirs(os.path.join(parent_dir, "DAILY", f"{month}", f"{day}.{month}.{year}", "SIDEPHOTOS" , SIDEPHOTOS[z]))


if isAyarlar is False:
    file = open('ayarlar.txt', 'w')
    file.write("[ALT SATIRA GUNLUK DOSYASININ GELECEGI KONUMU GIRIN]\n")
    file.write("\n")
    file.write("[ALT SATIRA KAC FOTOGRAFCI OLACAGINI GIRIN]\n")
    file.write("\n")
    file.write("[ALT SATIRLARA SIRASIYLA SATIR STAIR FOTOGRAFCILARIN TAGLARINI GIRIN]\n")
    file.close()
    exit()
