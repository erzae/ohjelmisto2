#tehtävä-1
class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print(f"Kirja {self.nimi}")
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumäärä}")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}")
        print(f"Päätoimittaja: {self.päätoimittaja}")

aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti_nro_6 = Kirja("Hytti n:0 6", "Rosa Liksom", 200)

aku_ankka.tulosta_tiedot()
print()
hytti_nro_6.tulosta_tiedot()

print("-----------------------------------------------")

#tehtävä-2
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämän_hetkinen_nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämän_hetkinen_nopeus = tämän_hetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka
    def kiihdytä(self, nopeuden_muutos):
        uusi_nopeus = self.tämän_hetkinen_nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.tämän_hetkinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tämän_hetkinen_nopeus = 0
        else:
            self.tämän_hetkinen_nopeus = uusi_nopeus
    def kulje(self, tunnit):
        self.kuljettu_matka += self.tämän_hetkinen_nopeus * tunnit

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko


sähköauto = Sähköauto("ABC-15", 180, 52.3)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sähköauto.kiihdytä(120)
polttomoottoriauto.kiihdytä(100)

sähköauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"Sähköauton ({sähköauto.rekisteritunnus}) kuljettu matka: {sähköauto.kuljettu_matka} km")
print(f"Polttomoottoriauton ({polttomoottoriauto.rekisteritunnus} kuljettu matka: {polttomoottoriauto.kuljettu_matka} km")