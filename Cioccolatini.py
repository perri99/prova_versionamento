from Cioccolato import Cioccolato

class Cioccolatino(Cioccolato):

    def __init__(self, tipo, cacao, forma, ripieno):
        super().__init__(tipo, cacao)
        self.forma = forma
        self.ripieno = ripieno
        self.costo = 2

    def produce(self):
        print("E' stato prodotto cioccolatino", self.tipo_cioccolato, 'con percentuale di cacao:(', self.cacao, '% ) di forma',
              self.forma, 'e ripieno di', self.ripieno)
        
if __name__ == '__main__':
    Gianduiotto = Cioccolatino('Gianduiotto', 30, 'rettangolare', 'gianduia')
    Gianduiotto .produce()