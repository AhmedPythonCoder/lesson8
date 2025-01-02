#IMPORT LIBRARIES
import pgzrun

#set the dimentions of the screen
WIDTH = 500
HEIGHT = 700
#set the title of the screen
TITLE = 'rectangle'

r = 232
g = 20
b = 213


def draw():
    #Rect(x,y,width,height) 
    #screen.draw.circle(pos,radius,(r,g,b)) 
    #Rect((0, 8),(700, 800) )
    rect =     Rect((WIDTH/2, HEIGHT/2),(400, 400) )
    rect.center=(WIDTH/2, HEIGHT/2)
    screen.draw.rect(rect, (r,g,b))
#draw()
pgzrun.go()