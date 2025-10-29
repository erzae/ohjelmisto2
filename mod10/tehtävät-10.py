#tehtävä-1
class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
        else:
            print("Hissi on jo ylimmässä kerroksessa. ")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
        else:
            print("Hissi on jo alimmassa kerroksessa. ")

    def siirry_kerrokseen(self, kohde_kerros):
        print(f"Hissi siirtyy kerrokseen {kohde_kerros}..")
        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()

hissi = Hissi(1, 10)
hissi.siirry_kerrokseen(5)
hissi.siirry_kerrokseen(1)

#tehtävä-2
class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = []
        for i in range(hissien_lkm):
            h = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(h)

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        if 0 != hissin_numero < len(self.hissit):
            print(f"\nHissi {hissin_numero} siirtyy kerrokseen {kohde_kerros}: ")
            self.hissit[hissin_numero].siirry_kerrokseen(kohde_kerros)
        else:
            print("Virhe: hissin numero ei ole sallittu")

talo = Talo(1, 10, 2)
talo.aja_hissiä(0, 5)
talo.aja_hissiä(1, 8)
talo.aja_hissiä(0, 1)