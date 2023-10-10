from tkinter import *
from functools import partial
from PIL import ImageTk
import PIL.Image
from mazo import *
class AppVentiuna:
    def __init__(self):
        self.fuente= "Helvetica"
        self.ventana=Tk()
        self.textoCasa= Label(self.ventana, text="Casa",font=(self.fuente,15), fg="dark green",bg="light green")
        self.canvaCasa=Canvas(width=750,height=150, bg="white")
        self.textoJugador= Label(self.ventana, text="Jugador",font=(self.fuente,15), fg="dark green",bg="light green")
        self.canvaJugador=Canvas(width=750,height=150, bg="white")

        self.iniciarJuego = Button(self.ventana, text="  Iniciar Juego  ", fg="black",font=(self.fuente,20), command=self.iniciar_juego)
        self.elegirEspanola = Button(self.ventana, text="  Mazo Español  ", fg="black",font=(self.fuente,20), command=self.elegir_mazo_espanol)
        self.elegirFrancesa = Button(self.ventana, text="  Mazo Frances  ", fg="black",font=(self.fuente,20), command=self.elegir_mazo_frances)

        self.spriteBaraja=PhotoImage(file="sprites/baraja.png")
        self.labelBaraja= Label(self.ventana, image=self.spriteBaraja)

    def inicio_programa(self):
        self.canvaCasa.place(x=200,y=50)
        self.textoCasa.place(x=200,y=25)
        self.canvaJugador.place(x=200,y=250)
        self.textoJugador.place(x=200,y=225)
        self.elegirEspanola.place(x=250,y=425)
        self.elegirFrancesa.place(x=550,y=425)
    
    def obtener_siguiente_posicion(self, mazo):
        if mazo==self.jugador:
            if self.iteracionJugador==0:
                self.posicionesJugador.append((25,25))
            else:
                x=self.posicionesJugador[self.iteracionJugador-1][0]
                y=25
                self.posicionesJugador.append((x+125,y))
        elif mazo==self.casa:
            if self.iteracionCasa==0:
                self.posicionesCasa.append((25,25))
            else:
                x=self.posicionesCasa[self.iteracionCasa-1][0]
                y=25
                self.posicionesCasa.append((x+125,y))

    def colocar_carta(self, mazo):
        if mazo==self.jugador:
            pass
        elif mazo==self.casa:
            pass

    def entregar_carta(self, mazo):
        if mazo==self.jugador:
            self.jugador.cartas.append(self.baraja.entregar_carta())
            image =PIL.Image.open(self.jugador.cartas[self.iteracionJugador].direccion)
            image = image.resize((75,100), PIL.Image.Resampling.LANCZOS)
            self.spriteJugador.append(ImageTk.PhotoImage(image))
            self.iteracionJugador+=1
        elif mazo==self.casa:
            self.casa.cartas.append(self.baraja.entregar_carta())
            image =PIL.Image.open(self.casa.cartas[self.iteracionCasa].direccion)
            image = image.resize((75,100), PIL.Image.Resampling.LANCZOS)
            self.spriteCasa.append(ImageTk.PhotoImage(image))
            self.iteracionCasa+=1

    

    def elegir_mazo_espanol(self):
        self.elegirEspanola.destroy()
        self.elegirFrancesa.destroy()
        self.baraja= MazoEspanol()
        self.iniciarJuego.place(x=450,y=425)

    def elegir_mazo_frances(self):
        self.elegirEspanola.destroy()
        self.elegirFrancesa.destroy()
        self.baraja= MazoFrances()
        self.iniciarJuego.place(x=450,y=425)

    def iniciar_juego(self):
        self.iniciarJuego.destroy()

        self.posicionesJugador=[]
        self.posicionesCasa=[]
        self.iteracionJugador=0
        self.iteracionCasa=0
        self.spriteJugador=[]
        self.spriteCasa=[]

        self.casa = Mazo(True)
        self.jugador = Mazo(True)

        for i in range(2):
            self.entregar_carta(self.casa)
            self.entregar_carta(self.jugador)

        #self.ventana.after(1000,partial(objeto.place ,x=x_act,y=y_act))

    def ejecutar(self):
        self.ventana.geometry("1000x500")
        self.ventana.title("Ventiuna")
        self.ventana.config(bg="light green")
        self.ventana.resizable(False,False)
        self.inicio_programa()
        
        self.ventana.mainloop()
        
if __name__=="__main__":
    j= AppVentiuna()
    j.ejecutar()
