import pygame
from pyg_btn import Button #Import the Button class
 
import sys
pygame.init()

#Button function
def x():
    print("Button pressed")

#Pygame window
window = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Pygamebtn")

#Button object ; Note this has to be out of the while loop!

button1 = Button(width = 140,height = 40,color =(30,30,30),hover_color = (29,49,80) )

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:  #This is important!
            button1.pressed = False # buttonx.pressed = False
            
    button1.place(window,x=420,y=300) #x,y coordinate of button
    button1.text(window,text="Click Me!",x=450,y=312,color=(155,110,124),size =16) #Text
    button1.function(x) #Execute function x upon clicking
    pygame.display.update()
