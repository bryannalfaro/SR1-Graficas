'''
Universidad del Valle de Guatemala
Graficas por computadora - Bryann Alfaro
'''
from gl import Renderer

r =  Renderer()
r.glInit()
r.glCreateWindow(1024,768)
r.glViewPort(0,0,60,100)
r.glClearColor(1,0.75,0.80)
r.glVertex(0,0)
r.glColor(0.85,0.125,0.125)
r.glVertex(1,1)
r.glColor(0.250,0.239,0.541)
r.glVertex(-1,-1)
r.glColor(0.905,0.498,0.152)
r.glVertex(1,-1)
r.glColor(0.043,0.537,0.486)
r.glVertex(-1,1)
r.glColor(0,0,0)


r.glFinish("output.bmp")