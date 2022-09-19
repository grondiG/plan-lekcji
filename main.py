from lekcja import Lekcja
from klasa import Klasa
from nauczyciel import Nauczyciel

liczba_sal = int(input("Liczba sal: "))
liczba_godzin = int(input("Liczba godzin: "))

przedmioty = []
print("Przedmioty:")
while True:
    temp = input(": ")

    if temp == "":
        break

    przedmioty.append(temp)

nauczyciele = []
i = 0
print("Nauczyciele: ")
while True:
    temp = input("imie: ")

    if temp == "":
        break

    ktore_przedmioty = []
    for j in range(len(przedmioty)):
        ktore_przedmioty.append(int(input(przedmioty[j] + ": ")))

    nauczyciele.append(Nauczyciel(i, temp, ktore_przedmioty))
    i = i + 1


klasy = []
print("Klasy: ")
while True:
    temp = input("nazwa klasy: ")

    if temp == "":
        break

    liczba_godzin_w_tygodniu = []

    for i in range(len(przedmioty)):
        print(przedmioty[i] + ": ")
        liczba_godzin_w_tygodniu.append(int(input("")))

    klasy.append(Klasa(temp, liczba_godzin_w_tygodniu))


lekcje = []
for i in range(5):
    lekcje.append([])
    for j in range(liczba_godzin):
        lekcje[i].append([])
        for k in range(liczba_sal):
            lekcje[i][j].append([])
            for x in klasy:
                for d in range(len(przedmioty)):
                    if x.ile_przedmitow_w_tygodniu[d] > 0:
                        print("cba")
                        for n in nauczyciele:
                            if n.przedmioty[d] == 1:
                                print("abc")
                                lekcje[i][j][k].append(Lekcja(n, d, x))
                                x.ile_przedmitow_w_tygodniu[d] = x.ile_przedmitow_w_tygodniu[d] - 1
                                break


for x in range(len(lekcje)):
    for y in range(len(lekcje[x])):
        for z in range(len(lekcje[x][y])):
            for o in lekcje[x][y][z]:
                print((x*liczba_godzin) + y, o.nauczyciel.imie, przedmioty[o.przedmiot], o.klasa.nazwa, z)





