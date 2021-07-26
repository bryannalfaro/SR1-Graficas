import struct

"""
Bryann Alfaro 19372
SR1 - GRAFICAS POR COMPUTADORA
References for conversions:
https://stackoverflow.com/questions/10848990/rgb-values-to-0-to-1-scale
https://docs.microsoft.com/en-us/windows/win32/opengl/glviewport

PUNTOS REALIZADOS:
05 puntos) Deben crear una función glInit() que inicialice cualquier objeto interno que requiera su software renderer
(05 puntos) Deben crear una función glCreateWindow(width, height) que inicialice su framebuffer con un tamaño (la imagen resultante va a ser de este tamaño
(10 puntos)  Deben crear una función glViewPort(x, y, width, height) que defina el área de la imagen sobre la que se va a poder dibujar (hint)
(20 puntos) Deben crear una función glClear() que llene el mapa de bits con un solo color
(10 puntos) Deben crear una función glClearColor(r, g, b) con la que se pueda cambiar el color con el que funciona glClear(). Los parámetros deben ser números en el rango de 0 a 1.
(30 puntos) Deben crear una función glVertex(x, y) que pueda cambiar el color de un punto de la pantalla. Las coordenadas x, y son relativas al viewport que definieron con glViewPort.
glVertex(0, 0) cambia el color del punto en el centro del viewport, glVertex(1, 1) en la esquina superior derecha. glVertex(-1, -1) la esquina inferior izquierda. (hint)
(15 puntos) Deben crear una función glColor(r, g, b) con la que se pueda cambiar el color con el que funciona glVertex(). Los parámetros deben ser números en el rango de 0 a 1.
(05 puntos) Deben crear una función glFinish() que escriba el archivo de imagen
"""
def char(c):
    return struct.pack('=c',c.encode('ascii'))

def word(w):
    #short
    return struct.pack('=h',w)

def dword(d):
    #long
    return struct.pack('=l',d)

#setting the function to get color with bytes
def color(r,g,b):
    return bytes([b,g,r])

BLACK = color(0,0,0)
WHITE = color(255,255,255)

class Renderer(object):
    def __init__(self):
        self.default_color = color(0,0,139)
        self.cl_color = BLACK

    def point(self, x, y):
        self.framebuffer[y][x] =self.default_color



    def glInit(self):
        pass

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.framebuffer = []

    def glViewPort(self, x, y, width, height):
        self.vp_x = x
        self.vp_y = y
        self.vp_width = width
        self.vp_height = height

    #Fill the bitmap
    def glClear(self):
        self.framebuffer = [
            [self.cl_color for x in range(self.width)] for y in range(self.height)
            ]

    def glClearColor(self, r,g,b):
        self.cl_color = color(int(r*255),int(g*255),int(b*255))
        self.glClear()

    def glVertex(self,x,y):
        #formula get from microsoft glViewport function
        x_pos = int((x+1)*(self.vp_width/2)+self.vp_x)
        y_pos = int((y+1)*(self.vp_height/2)+self.vp_y)
        self.point(x_pos,y_pos)

    #change color of vertex
    def glColor(self, r,g,b):
        self.default_color = color(int(r*255),int(g*255),int(b*255))

    def glFinish(self, filename):
        #bw means binary write
        f = open(filename, 'bw')
        #file header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14+40+ 3*(self.width*self.height)))
        f.write(dword(0))
        f.write(dword(14+40))

        #info header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(3*(self.width*self.height)))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        #bitmap
        for y in range(self.height):
            for x in range(self.width):
                f.write(self.framebuffer[y][x])

        f.close()