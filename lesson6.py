#IMPORT LIBRARIES
import pgzrun

#set the dimentions of the screen
WIDTH = 500
HEIGHT = 700
#set the title of the screen
TITLE = 'rectangle'


w = 400
h = 600
def draw():
        w = 80
        h = 40
        r = 255
        g = 100
        b = 255
        for i in range(30):

        #Rect(x,y,width,height) 
        #screen.draw.circle(pos,radius,(r,g,b)) 
        #Rect((0, 8),(700, 800) )
            rect =     Rect((WIDTH/2, HEIGHT/2 ),(w, h) )
            rect.center=(WIDTH/2, HEIGHT/2)
            screen.draw.rect(rect, (r,g,b))
            r = r-5
            g = g+5
            b = b-5
            w = w + 20 
            h = h + 10
#draw()
pgzrun.go()
