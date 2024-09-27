
from Cioccolatini import Cioccolatino
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
            return True
        else:
            print('Cioccolato finito')
            return False


Fab = Fabbrica()

prodotti = [CioccolataCalda('Latte', 50, 34, 34), 
            Tavoletta('Bianca', 50, 800, 'nocciole'), 
            Cioccolatino('Gianduiotto', 50, 'ret', 'giand')]*100


for prodotto in prodotti:
    check = Fab.produci(prodotto)
    if not check:
        print('Fabbrica chiusa')
        break


