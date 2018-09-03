import pygame as pg
import sys

class Muro(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface([32,32])
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0

class BuffoR(pg.sprite.Sprite):
	def __init__(self, img):
		pg.sprite.Sprite.__init__(self)
		self.image = img
		self.rect = self.image.get_rect()

class Premio(pg.sprite.Sprite):
	def __init__(self, img):
		pg.sprite.Sprite.__init__(self)
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x = 540
		self.rect.y = 168

class Semilla(pg.sprite.Sprite):
	def __init__(self, img):
		pg.sprite.Sprite.__init__(self)
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0

class Bloque(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface([350,50])
		self.image.fill((0,0,0))
		self.rect = self.image.get_rect()
		self.rect.x = 385
		self.rect.y = 328

class Vida(pg.sprite.Sprite):
	def __init__(self, img, a, b):
		pg.sprite.Sprite.__init__(self)
		self.m=img
		self.image=self.m[a][b]
		self.rect=self.image.get_rect()

class Jugador(pg.sprite.Sprite):
	def __init__(self, img_sprite, a,b):
		pg.sprite.Sprite.__init__(self)
		self.m=img_sprite
		self.image=self.m[a][b]
		self.rect=self.image.get_rect()
		self.a = a
		self.b = b
		self.dir = a
		self.i = b
		self.var_x = 0
		self.var_y = 0
		self.muros = None
		#self.premios = None
		#self.rivales = None
		self.nriv = 0
		self.puntaje = 0
		self.vidas = 1

	def GetPos(self):
		print (self.rect.x , self.rect.y)

	def BajarVida(self):
		self.vidas -= 1
		self.rect.x = 550
		self.rect.y = 400
		self.nriv = 0

	def update(self):
		self.rect.x+= self.var_x
		self.rect.y += self.var_y

		#Colisiones con muros
		#--------------------------------------------------------#
		ls_bl=pg.sprite.spritecollide(self,self.muros,False)
		for m in ls_bl:
			if self.var_x > 0:
				self.rect.right =m.rect.left
			if self.var_x <0:
				self.rect.left=m.rect.right



		ls_bl1=pg.sprite.spritecollide(self,self.muros,False)
		for m in ls_bl1:
			if self.var_y > 0:
				self.rect.bottom=m.rect.top
			if self.var_y <0:
				self.rect.top=m.rect.bottom
		'''
		#--------------------------------------------------------#
		#Premios
		ls_bp = pg.sprite.spritecollide(self, self.premios, True)
		for m in ls_bp:
			self.puntaje += 500

		#--------------------------------------------------------#
		'''

		if self.var_x !=0 or self.var_y !=0:
			if self.i < self.b + 2:
				self.i+=1
			else:
				self.i=self.b
		self.image=self.m[self.i][self.dir]

class Rival(pg.sprite.Sprite):
	def __init__(self, img_sprite, a,b):
		pg.sprite.Sprite.__init__(self)
		self.m=img_sprite
		self.image=self.m[a][b]
		self.rect=self.image.get_rect()
		self.a = a
		self.b = b
		self.dir = a
		self.i = b
		self.var_x = 0
		self.var_y = 0
		self.muros= None
		self.VarVel()
		self.cont = 0
		self.cont2 = 0
		self.buffos = None
		self.buff = False
		self.pjs = None
		self.semillas = None


	def VarVel(self):
		r = random.randint(0,3)
		if r == 0:
			self.var_x = -8
			self.var_y = 0
			self.dir = 1
		if r == 1:
			self.var_x = 0
			self.var_y = -8
			self.dir = 3
		if r == 2:
			self.var_x = 8
			self.var_y = 0
			self.dir = 2
		if r == 3:
			self.var_x = 0
			self.var_y = 8
			self.dir = 0
		'''
		if r == 4:
			self.var_x = -3
			self.var_y = -3
		if r == 5:
			self.var_x = 3
			self.var_y = -3
		if r == 6:
			self.var_x = 3
			self.var_y = 3
		if r == 7:
			self.var_x = -3
			self.var_y = 3
		'''
	def Buffado(self):
		self.i = 6
		self.b = 6
		self.cont = 1000
		self.buff = True


	def update(self):
		#self.var_x = 5
		self.rect.x+= self.var_x

		#Colisiones muros
		#--------------------------------------------------------#
		ls_bl=pg.sprite.spritecollide(self,self.muros,False)
		for m in ls_bl:
			if self.var_x > 0:
				self.rect.right = m.rect.left
			if self.var_x <0:
				self.rect.left = m.rect.right
			self.VarVel()

		#self.var_y = 5
		self.rect.y += self.var_y
		ls_bl1=pg.sprite.spritecollide(self,self.muros,False)
		for m in ls_bl1:
			if self.var_y > 0:
				self.rect.bottom=m.rect.top
			if self.var_y <0:
				self.rect.top=m.rect.bottom
			self.VarVel()

		if self.cont > 0:
			self.cont -= 1
		else:
			self.i = 3
			self.b = 3
			self.buff = False

		if self.cont2 < 100:
			self.cont2 += 1
		else:
			self.VarVel()
			self.cont2 = 0

		if self.rect.x > Ancho or self.rect.x < 0 or self.rect.y > Alto or self.rect.y < 0:
			self.rect.x = 512
			self.rect.y = 96


		#--------------------------------------------------------#
		'''
		if self.buff:
			ls_pb = pg.sprite.spritecollide(self, self.pjs, True)
			for m in ls_pb:
				m.vidas -= 1
		'''



		if self.var_x !=0 or self.var_y !=0:
			if self.i < self.b + 2:
				self.i+=1
			else:
				self.i=self.b
		self.image=self.m[self.i][self.dir]
