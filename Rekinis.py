class Rekinis:

    def __init__(self, dt_now, vards, velteksts, izmeri, cena):
        self.dt_now = dt_now
        self.vards = vards
        self.velteksts = velteksts
        self.izmeri = izmeri
        self.cena = cena

       

    def izdrukat(self):
        print(f"Rēķina izveidošanas laiks: {self.dt_now}, Klienta vārds {self.vards}, Veltījuma teksts: {self.velteksts}, Lādītes izmērs: {self.izmeri}, Darba samaksa: {self.darba_samaksa}, Produkta cena: {self.produkta_cena}, PVN summa: {self.PVN_summa}, Reikina summa: {self.rekina_summa}")

    def aprekins(self):   
        darba_samaksa = 15
        PVN = 21
        produkta_cena = self.izmeri / 3 * self.cena
        pvn_summa = (darba_samaksa + self.cena) * 21/100
        rekina_summa = (self.darba_samaksa + self.produkta_cena) + self.PVN_summa
    
    def saglabat(self):