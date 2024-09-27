
from Tavoletta import Tavoletta
from CioccolataCalda import CioccolataCalda


class Fabbrica:
    def __init__(self):
        self.prodotti = []
        self.costo_totale = 0

    def produci(self, Prodotto):
        self.costo_totale += Prodotto.get_costo()
        if self.costo_totale <= 100:
            Prodotto.produce()
        else:
            print('Cioccolato finito')

prodotti2 = [Tavoletta('Bianca', 50, 800, 'nocciole')]
Fab = Fabbrica()
for prodotto in prodotti2:
    Fab.produci(prodotto)
prodotti = [CioccolataCalda('Latte', 50, 34, 34)]


for prodotto in prodotti:
    Fab.produci(prodotto)

