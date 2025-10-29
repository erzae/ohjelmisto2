#tehtävät-1-3
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

uusi_auto = Auto("ABC-123", 142,)

print(f"Uuden auton rekisteritunnus on {uusi_auto.rekisteritunnus} ja huippunopeus {uusi_auto.huippunopeus}.")

print(f"Auton ominaisuudet ovat: {uusi_auto.rekisteritunnus}, {uusi_auto.huippunopeus}, "
      f"{uusi_auto.kuljettu_matka}km/h ja {uusi_auto.tämän_hetkinen_nopeus}km/h.")


uusi_auto.kiihdytä(30)
uusi_auto.kiihdytä(70)
uusi_auto.kiihdytä(50)
print(f"Nopeus kiihdytyksen jälkeen: {uusi_auto.tämän_hetkinen_nopeus} km/h")

uusi_auto.kulje(1.5)
print(f"Kuljettu matka ajon jälkeen: {uusi_auto.kuljettu_matka} km/h")

uusi_auto.kiihdytä(-200)
print(f"Nopeus hätäjarrutuksen jälkeen: {uusi_auto.tämän_hetkinen_nopeus} km/h")




