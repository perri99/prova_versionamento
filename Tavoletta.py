from Cioccolato import Cioccolato

class Tavoletta(Cioccolato):

    def __init__(self, tipo, cacao, peso, *aggiunte):
        super().__init__(tipo, cacao)
        self.peso = peso
        self.aggiunte = aggiunte
        costo = 4 + peso/50
        if costo <= 24: self.costo = costo
        else: self.costo = 24

    def produce(self):
        print("E' stata prodotta tavoletta", self.tipo_cioccolato, 'con percentuale di cacao:(', self.cacao, '% ) di peso',
              self.peso, 'con aggiunta di', self.aggiunte, 'costo:', self.costo)
        
    
if __name__ == '__main__':
    Tavoletta_bianca = Tavoletta('Bianca', 20, 8000, 'nocciola', 'mandorle')
    Tavoletta_bianca.produce()