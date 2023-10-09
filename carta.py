class Carta:
    def __init__(self, valor, pinta):
        self.pinta = pinta
        self.valor = valor
        self.asignar_direccion()

    def asignar_direccion(self):
        str1=self.pinta
        for i in [str(x) for x in range(2,11)] + ['A', 'J', 'Q', 'K']:
            if i==self.valor:
                str2=i
        self.direccion=("sprites/"+str1+"/"+str2+".png")

    def obtener_valor(self):
        if self.valor == 'A':
            return 1
        if self.valor in ['J', 'Q', 'K']:
            return 10
        return int(self.valor)

    def mostrar_carta(self):
        return self.pinta, self.valor
    
class CartaFrancesa(Carta):
    pass

class CartaEspanola(Carta):
    pass
