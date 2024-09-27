from Tavoletta import Tavoletta

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

prodotti = [Tavoletta('Bianca', 50, 800, 'nocciole')]
Fab = Fabbrica()
for prodotto in prodotti:
    Fab.produci(prodotto)