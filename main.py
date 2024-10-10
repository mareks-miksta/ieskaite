import Rekinis as rek
import datetime

dt_now = datetime.datetime.now()

vards = input("Uzraksti vārdu: ")

velteksts = input("Veltījuma teksts: ")

izmerip = int(input("Lādītes izmēri (platums milimetros): "))

izmerig = int(input("Lādītes izmēri (garums milimetros): "))

izmeria = int(input("Lādītes izmēri (augstums milimetros): "))

izmeri = (izmerip * izmerig * izmeria)

cena = int(input("Kokmateriāla cena (EUR/m 2): "))

ladite1 = rek.Rekinis(dt_now, vards, velteksts, [izmerip, izmerig, izmeria], cena)


