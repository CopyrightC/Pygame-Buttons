import sys
import pygame
from threading import Thread

pygame.init()


class Button:

	def __init__(self,
	width = 120,
	height = 40,
	color = (255,0,0),
	hover_color = (0,255,0),):
	    
	    self.hover_color = hover_color
	    self.color = color
	    self.color_copy = color
	    self.width = width
	    self.height = height
	    self.called = False
	    self.rect = pygame.Rect(10,10,self.width,self.height)
	    self.booly = True

	def place(self,window,x,y):
	    pygame.draw.rect(window,self.color,self.rect)
	    if not self.called:
		Thread(target=self.hover,args=(x,y,x+self.width,y+self.height)).start()
		self.called = True

	def text(self,screen,text,x,y,font ="freesansbold.ttf",size=34,antialias=True,color = (0,0,0)):
	    fontx = pygame.font.Font(font,size)
	    txt = fontx.render(text,antialias,color)
	    screen.blit(txt,(x,y))
		
	def hover(self,x1,y1,x2,y2):
	    self.called = True
	    try:
		while True:
		    pos = pygame.mouse.get_pos()
		    if self.rect.collidepoint(pos):
			self.color = self.hover_color

		    else:
			self.color = self.color_copy
	   except pygame.error:
		pass
	
	def function(self,command = None):
	    if command == None:
		pygame.quit()
		raise TypeError("Command can't be a NoneType object")
	    try:
		if event.type == pygame.MOUSEBUTTONDOWN:
		    if self.booly:
			command()
			self.booly = False
		if event.type == pygame.MOUSEBUTTONUP:
		    self.booly = True

	    except:
		raise Exception("Unknown error")
