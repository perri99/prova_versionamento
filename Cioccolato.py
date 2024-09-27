
class Cioccolato:

    def __init__(self, tipo, cacao):
        if type(tipo) == str: self.tipo_cioccolato = tipo
        else: print('Il tipo di cioccolato deve essere', type('c'))
        if type(cacao) == int : self.cacao = cacao
        else: print('La percentuale di cacao deve essere di tipo', type(1))
        self.costo = 0
        self.max = 100

    def produce(self):
        print("E' stato prodotto cioccolato", self.tipo_cioccolato, 'con percentuale di cacao:', self.cacao, '%')

    def get_costo(self):
        return self.costo

if __name__ == '__main__':
    Bianco = Cioccolato('Bianco', 40)
    Bianco.produce()

    

