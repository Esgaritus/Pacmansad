import pygame as pg
import sys

def Recortar(archivo, an,al):
	fondo = pg.image.load(archivo).convert_alpha()
	info=fondo.get_size()
	img_ancho=info[0]
	img_alto=info[1]
	corte_x=img_ancho/an
	corte_y=img_alto/al

	m=[]
	for i in range(an):
		fila=[]
		for j in range(al):
			cuadro=[i*corte_x,j*corte_y,corte_x,corte_y]
			recorte = fondo.subsurface(cuadro)
			fila.append(recorte)
		m.append(fila)

	return m

def Mapping(fondo, mapa, interprete, pantalla):
	y = 0
	l = 0
	pantalla.fill((0,0,0))
	for f in mapa:
			for e in f:
				ax = int(interprete.get(e,'x'))
				ay = int(interprete.get(e,'y'))
				#a = int(a)
				#b = int(b)
				pantalla.blit(fondo[ax][ay],[l,y])

				l += 32
			y += 32
			l= 0
