from tkinter import *
from functools import partial
from PIL import ImageTk
import PIL.Image
from tkinter import messagebox
from mazo import *
class AppVentiuna:
    def __init__(self):
        self.fuente= "Helvetica"
        self.ventana=Tk()
        self.textoCasa= Label(self.ventana, text="Casa",font=(self.fuente,15), fg="dark green",bg="light green")
        self.puntuacionCasa = Label(self.ventana, text="Puntuación: ",font=(self.fuente,15), fg="dark green",bg="light green")
        self.canvaCasa=Canvas(width=750,height=150, bg="white")
        
        self.textoJugador= Label(self.ventana, text="Jugador",font=(self.fuente,15), fg="dark green",bg="light green")
        self.puntuacionJugador = Label(self.ventana, text="Puntuación: ",font=(self.fuente,15), fg="dark green",bg="light green")
        self.canvaJugador=Canvas(width=750,height=150, bg="white")

        self.iniciarJuego = Button(self.ventana, text="  Iniciar Juego  ", fg="black",font=(self.fuente,20), command=self.iniciar_juego)
        self.elegirEspanola = Button(self.ventana, text="  Mazo Español  ", fg="black",font=(self.fuente,20), command=self.elegir_mazo_espanol)
        self.elegirFrancesa = Button(self.ventana, text="  Mazo Frances  ", fg="black",font=(self.fuente,20), command=self.elegir_mazo_frances)
        self.pedirCarta =Button(self.ventana, text="  Pedir Carta  ", fg="black",font=(self.fuente,20), command=self.pedir_carta)
        self.plantar =Button(self.ventana, text="  Plantarse  ", fg="black",font=(self.fuente,20), command=self.plantarse)
        self.siguienteCasa=Button(self.ventana, text="  Siguiente  ", fg="black",font=(self.fuente,20), command=self.sig_casa)
        self.saltarCasa=Button(self.ventana, text="  Saltar  ", fg="black",font=(self.fuente,20), command=self.skip)
        self.tryAgain =Button(self.ventana, text="  Jugar de Nuevo  ", fg="black",font=(self.fuente,20), command=self.inicio_programa)

        self.spriteBaraja=PhotoImage(file="sprites/baraja.png")
        self.labelBaraja= Label(self.ventana, image=self.spriteBaraja)

        self.reinicio_condiciones()

    def inicio_programa(self):
        self.tryAgain.place_forget()
        self.borrar_imagenes_cartas()
        self.puntuacionCasa.config(text="Puntuación: ")
        self.puntuacionJugador.config(text="Puntuación: ")
        self.canvaCasa.place(x=200,y=50)
        self.textoCasa.place(x=200,y=25)
        self.puntuacionCasa.place(x=450,y=25)
        self.canvaJugador.place(x=200,y=250)
        self.textoJugador.place(x=200,y=225)
        self.puntuacionJugador.place(x=450,y=225)
        self.elegirEspanola.place(x=250,y=425)
        self.elegirFrancesa.place(x=550,y=425)

    def reinicio_condiciones(self):
        self.juegoPerdido=False
        self.juegoTerminado=False
        self.rondaJugador=True
        self.posicionesJugador=[]
        self.posicionesCasa=[]
        self.iteracionJugador=0
        self.iteracionCasa=0
        self.spriteJugador=[]
        self.spriteCasa=[]
        self.labelsJugador=[]
        self.labelsCasa=[]
    
    def elegir_mazo_espanol(self):
        self.elegirEspanola.place_forget()
        self.elegirFrancesa.place_forget()
        self.baraja= MazoEspanol()
        self.iniciarJuego.place(x=450,y=425)

    def elegir_mazo_frances(self):
        self.elegirEspanola.place_forget()
        self.elegirFrancesa.place_forget()
        self.baraja= MazoFrances()
        self.iniciarJuego.place(x=450,y=425)

    def borrar_imagenes_cartas(self):
        for i in range(self.iteracionCasa):
            self.labelsCasa[i].destroy()
        for i in range(self.iteracionJugador):
            self.labelsJugador[i].destroy()

    def obtener_posicion(self, mazo):
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
            label= Label(self.canvaJugador,image=self.spriteJugador[self.iteracionJugador])
            self.labelsJugador.append(label)
            self.obtener_posicion(self.jugador)
            x_l=self.posicionesJugador[self.iteracionJugador][0]
            y_l=self.posicionesJugador[self.iteracionJugador][1]
            self.labelsJugador[self.iteracionJugador].place(x=x_l,y=y_l)

        elif mazo==self.casa:
            label= Label(self.canvaCasa,image=self.spriteCasa[self.iteracionCasa])
            self.labelsCasa.append(label)
            self.obtener_posicion(self.casa)
            x_l=self.posicionesCasa[self.iteracionCasa][0]
            y_l=self.posicionesCasa[self.iteracionCasa][1]
            self.labelsCasa[self.iteracionCasa].place(x=x_l,y=y_l)

    def entregar_carta(self, mazo):
        if mazo==self.jugador:
            self.jugador.cartas.append(self.baraja.entregar_carta())
            image =PIL.Image.open(self.jugador.cartas[self.iteracionJugador].direccion)
            image = image.resize((75,100), PIL.Image.Resampling.LANCZOS)
            self.spriteJugador.append(ImageTk.PhotoImage(image))
            self.colocar_carta(mazo)
            self.iteracionJugador+=1
        elif mazo==self.casa:
            self.casa.cartas.append(self.baraja.entregar_carta())
            image =PIL.Image.open(self.casa.cartas[self.iteracionCasa].direccion)
            image = image.resize((75,100), PIL.Image.Resampling.LANCZOS)
            self.spriteCasa.append(ImageTk.PhotoImage(image))
            self.colocar_carta(mazo)
            self.iteracionCasa+=1
    
    def actualizar_puntuaciones(self):
        self.puntuacionCasa.config(text="Puntuación: "+ str(self.casa.obtener_valor_mazo()))
        self.puntuacionJugador.config(text="Puntuación: "+ str(self.jugador.obtener_valor_mazo()))

    def valorar_juego(self):
        valor_casa = self.casa.obtener_valor_mazo()
        valor_jugador = self.jugador.obtener_valor_mazo()

        if valor_jugador > 21:
            self.juegoPerdido=True
            self.juegoTerminado=True
        else: 
            if valor_casa >= valor_jugador and valor_casa<22 and self.rondaJugador==False:
                self.juegoPerdido=True
                self.juegoTerminado=True
            elif valor_casa > 21:
                self.juegoTerminado=True

        if self.juegoTerminado:
            self.pedirCarta.place_forget()
            self.plantar.place_forget()
            self.labelBaraja.place_forget()
            self.siguienteCasa.place_forget()
            self.saltarCasa.place_forget()
            if self.juegoPerdido:
                messagebox.showinfo("La casa gana", "La casa gana. Mejor suerte a la proxima")
            else:
                messagebox.showinfo("El jugador gana", "El jugador gana. ¡Felicidades!")
            self.tryAgain.place(x=450,y=425)

    def pedir_carta(self):
        self.entregar_carta(self.jugador)
        self.actualizar_puntuaciones()
        self.valorar_juego()

    def plantarse(self):
        self.pedirCarta.place_forget()
        self.plantar.place_forget()
        self.labelBaraja.place(x=50,y=75)
        self.siguienteCasa.place(x=250,y=425)
        self.saltarCasa.place(x=550,y=425)
        self.rondaJugador=False
        self.valorar_juego()

    def sig_casa(self):
        self.valorar_juego()
        if self.juegoPerdido==False:
            self.entregar_carta(self.casa)
        self.actualizar_puntuaciones()
        self.valorar_juego()
        
    def skip(self):
        while self.juegoTerminado==False:
            self.valorar_juego()
            if self.juegoTerminado==False:
                self.entregar_carta(self.casa)
                self.actualizar_puntuaciones()
            
    def iniciar_juego(self):
        self.iniciarJuego.place_forget()
        self.pedirCarta.place(x=250,y=425)
        self.plantar.place(x=550,y=425)
        self.labelBaraja.place(x=50,y=275)

        self.casa = Mazo(True)
        self.jugador = Mazo(True)

        self.reinicio_condiciones()
        
        for i in range(2):
            self.entregar_carta(self.casa)
            self.entregar_carta(self.jugador)
        self.actualizar_puntuaciones()

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
