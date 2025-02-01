import random
dol = int(input("podaj dolny zakres: "))
gora = int(input("podaj gorny zakres: "))
if dol > gora:
    print("dol nie moze byc wiekszy od góry jełopie :)")
    exit()
los = random.randint(dol, gora)
los_maly = int(max(los*0.8, dol))
los_duzy = int(min(los*1.2, gora))
proby = 0
while True:
    x = int(input("podaj liczbe: "))
    proby += 1
    if x > gora:
        print("wychodzi poza zakres!")
        break
    if proby > 10:
        print("za duzo prob!")
        break
    if x > los:
        print("za duzo")
        print(f"liczba ta znajduje sie miedzy {los_maly} a {los_duzy}")
    elif x < los:
        print("za malo")
        print(f"liczba ta znajduje sie miedzy {los_maly} a {los_duzy}")
    else:
        print(f"gratulacje udalo ci sie odgadgnoc liczbe w {proby} probach!")
        break
