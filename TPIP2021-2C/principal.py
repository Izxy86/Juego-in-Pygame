
import os, random, sys, math

import pygame
from pygame.locals import *
from configuracion import *
from funcionesVACIAS import *
from extras import *


#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()


        #pygame.mixer.init()
        musicaAmbiente()

        #Preparar la ventana
        pygame.display.set_caption("Armar Países...")
        screen = pygame.display.set_mode((ANCHO, ALTO))
        fondo= pygame.image.load("fondo-negro.jpg").convert()
        #tiempo total del juego
        gameClock = pygame.time.Clock()

        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial




        puntos = 0
        candidata = ""
        listaIzq = []
        listaMedio = []
        listaDer = []
        posicionesIzq = []
        posicionesMedio = []
        posicionesDer = []
        lista = []

        archivo= open("lemario.txt","r",encoding='latin-1')
        for linea in archivo.readlines():
            lista.append(linea[0:-1])

        cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer)
        dibujar(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq ,
                posicionesMedio, posicionesDer, puntos,segundos)


        verdad= False
        pagina=1

    ##### Pantalla de Presentación ###############
        screen.blit(fondo,[0,0])
        pygame.display.update()
        while not verdad :
            for evento in pygame.event.get(): #Capta instrucciones del teclado o mouse
                if evento.type == pygame.QUIT:
                     pygame.quit()
                     verdad= True
                if evento.type == pygame.MOUSEBUTTONDOWN: # Espera el click del usuario
                    pygame.display.flip()
                    verdad=True # Salimos del bucle



            # Limpia la pantalla y establece su color de fondo

            fondojuego= pygame.image.load("fondojuego.jpg").convert()
            screen.blit(fondojuego,[0,0])
            pygame.display.update()










        game_over = pygame.image.load("gameover.jpg").convert()
        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()



            if True:
            	fps = 3

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    candidata += letra
                    if e.key == K_BACKSPACE:
                        candidata = candidata[0:len(candidata)-1]
                    if e.key == K_RETURN:
                        puntos += procesar(lista, candidata, listaIzq, listaMedio, listaDer)

                        candidata = ""

            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)
            screen.blit(fondo,[0,0])

            #Dibujar de nuevo todo
            dibujar(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq ,
                posicionesMedio, posicionesDer, puntos,segundos)

            pygame.display.flip()

            actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq,
                posicionesMedio, posicionesDer)

        screen.blit(game_over,[0,0])
        gameOver()
        fuente=pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
        texto = fuente.render("Gracias Por Jugar", True, COLOR_TEXTO_FINAL)
        screen.blit(texto, [300, 420])
        texto1= fuente.render ("Puntuación Final:",True,COLOR_TEXTO_FINAL)
        a=str(puntos)
        texto2= fuente.render(a,True,COLOR_TEXTO_FINAL)
        screen.blit(texto1,[300,450])
        screen.blit(texto2,[380,480])
        pygame.display.update()
        while 1:



            for e in pygame.event.get():


                if e.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    return

##Programa Principal ejecuta Main
if __name__ == "__main__":
    main()



