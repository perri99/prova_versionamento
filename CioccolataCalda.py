from Cioccolato import Cioccolato

class CioccolataCalda(Cioccolato):

    def __init__(self, tipo, cacao, temperatura, densità):
        super().__init__(tipo, cacao)
        self.temperatura = temperatura
        self.densità = densità
        self.costo = 20

    def produce(self):
        print('Prodotta cioccolata calda:', self.tipo_cioccolato, 'temperatura:', self.temperatura, 'densità', self.densità,
              'costo:', self.costo)
        

if __name__ == '__main__':
    CC = CioccolataCalda('Latte', 50, 45, 1000)
    CC.produce()