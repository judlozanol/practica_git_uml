from mazo import *

class Juego:
    def __init__(self, mazo):
        self.mazo = mazo
        self.jugador1 = Mazo(True)
        self.jugador2 = Mazo(True)

    def iniciar_juego(self):
        for i in range(2):
            self.jugador1.cartas.append(self.mazo.entregar_carta())
            self.jugador2.cartas.append(self.mazo.entregar_carta())

    def mostrar_juego(self):
        print("Casa:")
        self.jugador1.mostrar_cartas()
        print("Valor mano: ", self.jugador1.obtener_valor_mazo())

        print("Jugador:")
        self.jugador2.mostrar_cartas()
        print("Valor mano: ", self.jugador2.obtener_valor_mazo())
       

    def valorar_juego(self):
        valor_casa = self.jugador1.obtener_valor_mazo()
        valor_jugador = self.jugador2.obtener_valor_mazo()

        if valor_jugador > valor_casa and valor_jugador <= 21:
            print("Jugador gana")
        elif valor_jugador <= 21 and valor_casa > 21:
            print("Jugador gana")
        elif valor_casa <= 21:
            print("Casa gana")

    def jugar(self):
        while self.jugador2.obtener_valor_mazo() < 18:
            self.jugador2.cartas.append(self.mazo.entregar_carta())
            self.mostrar_juego()
        while self.jugador1.obtener_valor_mazo() < self.jugador2.obtener_valor_mazo() and self.jugador1.obtener_valor_mazo() < 21 and self.jugador2.obtener_valor_mazo() <= 21:
            self.jugador1.cartas.append(self.mazo.entregar_carta())
            self.mostrar_juego()


if __name__ == "__main__":
    j = Juego(MazoEspanol())
    j.iniciar_juego()
    j.jugar()
    j.valorar_juego()
    