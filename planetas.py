from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
from math import cos, sin



def load_texture(texture_file):

    textureSurface = pygame.image.load(texture_file)
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()
    
    glEnable(GL_TEXTURE_2D)
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texture


class Fundo():

    def __init__(self, textura):
        self.textura = textura


    def desenha(self):
        glBindTexture(GL_TEXTURE_2D, self.textura)

        glColor3f(1, 1, 1)

        glPushMatrix()
    
        glBegin(GL_QUADS)

        glTexCoord2f(0, 0); glVertex3f(-30, -30, -30)
        glTexCoord2f(0, 1); glVertex3f(-30, 30, -30)
        glTexCoord2f(1, 1); glVertex3f(30, 30, -30)
        glTexCoord2f(1, 0); glVertex3f(30, -30, -30)
        

         #frente
        glTexCoord2f(0, 0); glVertex3f(-30, -30, 30)
        glTexCoord2f(0, 1); glVertex3f( 30, -30, 30)
        glTexCoord2f(1, 1); glVertex3f( 30,  30, 30)
        glTexCoord2f(1, 0); glVertex3f(-30,  30, 30)

        #lado esquerdo
        glTexCoord2f(0, 0); glVertex3f(-30, -30, 30)
        glTexCoord2f(0, 1); glVertex3f(-30, 30, 30)
        glTexCoord2f(1, 1); glVertex3f(-30, 30, -30)
        glTexCoord2f(1, 0); glVertex3f(-30, -30, -30)

        #baixo
        glTexCoord2f(0, 0); glVertex3f(-30, -30, 30)
        glTexCoord2f(0, 1); glVertex3f(30, -30, 30)
        glTexCoord2f(1, 1); glVertex3f(30, -30, -30)
        glTexCoord2f(1, 0); glVertex3f(-30, -30, -30)
        

        #tras
        glTexCoord2f(0, 0); glVertex3f(30,  30, -30)
        glTexCoord2f(0, 1); glVertex3f(30, -30, -30)
        glTexCoord2f(1, 1); glVertex3f(-30, -30, -30)
        glTexCoord2f(1, 0); glVertex3f(-30,  30, -30)

        #lado direito
        glTexCoord2f(0, 0); glVertex3f(30, 30, -30)
        glTexCoord2f(0, 1); glVertex3f(30, 30, 30)
        glTexCoord2f(1, 1); glVertex3f(30, -30, 30)
        glTexCoord2f(1, 0); glVertex3f(30, -30, -30)

        #cima
        glTexCoord2f(0, 0); glVertex3f(30, 30, -30)
        glTexCoord2f(0, 1); glVertex3f(-30, 30, -30)
        glTexCoord2f(1, 1); glVertex3f(-30, 30, 30)
        glTexCoord2f(1, 0); glVertex3f(30, 30, 30)

        glEnd()
        glPopMatrix()


class Sol():

    
    def __init__(self, textura):
        self.textura = textura

    def desenha(self, angulo):

        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslate(0, 0, 0)

        glBindTexture(GL_TEXTURE_2D, self.textura) # Vincula a textura
        # glRotate(-90, 1, 0, 0)
        # glRotate(angulo, 0, 0, 1)
        quadric = gluNewQuadric()
        gluQuadricTexture(quadric, GL_TRUE) # Habilita mapeamento de textura para a esfera
        gluSphere(quadric, 0.40, 100, 100) # Desenha a esfera
        glPopMatrix()

class Mercurio():

    def __init__(self, textura):
        self.textura = textura
       

    def desenha(self, angulo):
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(-0.5, 0, 0.5)
            
        glBindTexture(GL_TEXTURE_2D, self.textura) 
        glRotate(-90, 1, 0, 0)
        glRotate(angulo, 0, 0, 1)
        quadric = gluNewQuadric()
        gluQuadricTexture(quadric, GL_TRUE)
        gluSphere(quadric, 0.05, 100, 100) 
        glPopMatrix()

    def orbita(self):
        radius, num_segments, height = 0.7, 100, 0
        glBegin(GL_LINE_LOOP)
        for i in range(num_segments):
            theta = 2.0 * 3.1415926 * i / num_segments
            x = radius * cos(theta)
            y = radius * sin(theta)
            glVertex3f(x, y, height)
        glEnd()


class Venus():

    def __init__(self, textura):
        self.textura = textura

    def desenha(self, angulo):
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(-0.8, 0, 0.8)
            
        glBindTexture(GL_TEXTURE_2D, self.textura) 
        glRotate(-90, 1, 0, 0)
        glRotate(angulo, 0, 0, 1)
        quadric = gluNewQuadric()
        gluQuadricTexture(quadric, GL_TRUE)
        gluSphere(quadric, 0.09, 100, 100) 
        glPopMatrix()

    def orbita(self):
        radius, num_segments, height = 1.1, 100, 0
        glBegin(GL_LINE_LOOP)
        for i in range(num_segments):
            theta = 2.0 * 3.1415926 * i / num_segments
            x = radius * cos(theta)
            y = radius * sin(theta)
            glVertex3f(x, y, height)
        glEnd()


class Terra():

    def __init__(self, textura, textura_lua, n_luas):
        self.textura = textura
        self.textura_lua = textura_lua
        self.n_luas = n_luas


    def desenha(self, angulo):
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(-1.2, 0, 1.2)
            
        glBindTexture(GL_TEXTURE_2D, self.textura) 
        glRotate(-90, 1, 0, 0)
        glRotate(angulo, 0, 0, 1)
        quadric = gluNewQuadric()
        gluQuadricTexture(quadric, GL_TRUE)
        gluSphere(quadric, 0.12, 100, 100) 
        self.desenha_lua(angulo)
        glPopMatrix()

    def orbita(self):
        radius, num_segments, height = 1.7, 100, 0
        glBegin(GL_LINE_LOOP)
        for i in range(num_segments):
            theta = 2.0 * 3.1415926 * i / num_segments
            x = radius * cos(theta)
            y = radius * sin(theta)
            glVertex3f(x, y, height)
        glEnd()

    def desenha_lua(self, angulo):
        translate = 0.15
        for _ in range(self.n_luas):
            glTranslatef(-translate, 0, translate)

            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
            glEnable(GL_DEPTH_TEST)
            glPushMatrix()
            glBindTexture(GL_TEXTURE_2D, self.textura_lua) 
            glRotate(-90, 1, 0, 0)
            glRotate(angulo, 0, 0, 1)
            # glRotate(-angulo, 1, 1 ,1)
            quadric = gluNewQuadric()
            gluQuadricTexture(quadric, GL_TRUE)
            gluSphere(quadric, 0.02, 100, 100) 
            if self.n_luas > 1:
                translate * -3
            glPopMatrix()


class Marte():

    def __init__(self, textura, textura_lua, n_luas):
        self.textura = textura
        self.textura_lua = textura_lua
        self.n_luas = n_luas

    def desenha(self, angulo):
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(-1.5, 0, 1.5)
        glBindTexture(GL_TEXTURE_2D, self.textura) 
        glRotate(-90, 1, 0, 0)
        glRotate(angulo, 0, 0, 1)
        quadric = gluNewQuadric()
        gluQuadricTexture(quadric, GL_TRUE)
        gluSphere(quadric, 0.07, 100, 100) 
        self.desenha_lua(angulo)
        glPopMatrix()

    def orbita(self):
        radius, num_segments, height = 2.1, 100, 0
        glBegin(GL_LINE_LOOP)
        for i in range(num_segments):
            theta = 2.0 * 3.1415926 * i / num_segments
            x = radius * cos(theta)
            y = radius * sin(theta)
            glVertex3f(x, y, height)
        glEnd()

    def desenha_lua(self, angulo):
        translate = 0.1
        for _ in range(self.n_luas):
            glTranslatef(-translate, 0, translate)

            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
            glEnable(GL_DEPTH_TEST)
            glPushMatrix()
            glBindTexture(GL_TEXTURE_2D, self.textura_lua) 
            quadric = gluNewQuadric()
            gluQuadricTexture(quadric, GL_TRUE)
            gluSphere(quadric, 0.02, 100, 100) 
            if self.n_luas > 1:
                translate = -0.2
            glPopMatrix()


class Jupiter():

    def __init__(self, textura, textura_lua, n_luas):
        self.textura = textura
        self.textura_lua = textura_lua
        self.n_luas = n_luas

    def desenha(self, angulo):
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(-1.8, 0, 1.8)
        glBindTexture(GL_TEXTURE_2D, self.textura) 
        glRotate(-90, 1, 0, 0)
        glRotate(angulo, 0, 0, 1)
        quadric = gluNewQuadric()
        gluQuadricTexture(quadric, GL_TRUE)
        gluSphere(quadric, 0.18, 100, 100) 
        self.desenha_lua(angulo)
        glPopMatrix()


    def orbita(self):
        radius, num_segments, height = 2.6, 100, 0
        glBegin(GL_LINE_LOOP)
        for i in range(num_segments):
            theta = 2.0 * 3.1415926 * i / num_segments
            x = radius * cos(theta)
            y = radius * sin(theta)
            glVertex3f(x, y, height)
        glEnd()

    def desenha_lua(self, angulo):
        translate = 0.2
        for _ in range(self.n_luas):
            glTranslatef(-translate, 0, translate)

            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
            glEnable(GL_DEPTH_TEST)
            glPushMatrix()
            glBindTexture(GL_TEXTURE_2D, self.textura_lua) 
            glRotate(-90, 1, 0, 0)
            glRotate(angulo, 0, 0, 1)
            quadric = gluNewQuadric()
            gluQuadricTexture(quadric, GL_TRUE)
            gluSphere(quadric, 0.02, 100, 100) 
            if self.n_luas > 1:
                translate = -0.4
            glPopMatrix()


class Saturno():

    def __init__(self, textura, textura_anel, textura_lua, n_luas):
        self.textura = textura
        self.textura_anel = textura_anel
        self.textura_lua = textura_lua
        self.n_luas = n_luas

    def desenha(self, angulo):
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(-2.1, 0, 2.1)
        glBindTexture(GL_TEXTURE_2D, self.textura) 
        glRotate(-90, 1, 0, 0)
        glRotate(angulo, 0, 0, 1)
        quadric = gluNewQuadric()
        gluQuadricTexture(quadric, GL_TRUE)
        gluSphere(quadric, 0.13, 100, 100) 
        glRotate(-30, 1, 0, 0)
        self.aneis()
        self.desenha_lua(angulo)
        glPopMatrix()

    def aneis(self):
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glEnable(GL_DEPTH_TEST)
        glBindTexture(GL_TEXTURE_2D, self.textura_anel)
        disco = gluNewQuadric()
        gluQuadricTexture(disco, GL_TRUE)
        gluDisk(disco, 0.18, 0.24, 100, 1)

    def orbita(self):
        radius, num_segments, height = 3, 100, 0
        glBegin(GL_LINE_LOOP)
        for i in range(num_segments):
            theta = 2.0 * 3.1415926 * i / num_segments
            x = radius * cos(theta)
            y = radius * sin(theta)
            glVertex3f(x, y, height)
        glEnd()

    def desenha_lua(self, angulo):
        translate = 0.2
        for _ in range(self.n_luas):
            glTranslatef(-translate, 0, translate)

            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
            glEnable(GL_DEPTH_TEST)
            glPushMatrix()
            glBindTexture(GL_TEXTURE_2D, self.textura_lua) 
            glRotate(-90, 1, 0, 0)
            glRotate(angulo, 0, 0, 1)
            quadric = gluNewQuadric()
            gluQuadricTexture(quadric, GL_TRUE)
            gluSphere(quadric, 0.02, 100, 100) 
            if self.n_luas > 1:
                translate = -0.4
            glPopMatrix()

class Urano():
    def __init__(self, textura, textura_lua, n_luas):
        self.textura = textura
        self.textura_lua = textura_lua
        self.n_luas = n_luas

    def desenha(self, angulo):
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(-2.7, 0, 2.7)
        glBindTexture(GL_TEXTURE_2D, self.textura) 
        glRotate(-90, 1, 0, 0)
        glRotate(angulo, 0, 0, 1)
        quadric = gluNewQuadric()
        gluQuadricTexture(quadric, GL_TRUE)
        gluSphere(quadric, 0.12, 100, 100) 
        self.desenha_lua(angulo)
        glPopMatrix()


    def orbita(self):
        radius, num_segments, height = 3.8, 100, 0
        glBegin(GL_LINE_LOOP)
        for i in range(num_segments):
            theta = 2.0 * 3.1415926 * i / num_segments
            x = radius * cos(theta)
            y = radius * sin(theta)
            glVertex3f(x, y, height)
        glEnd()

    def desenha_lua(self, angulo):
        translate = 0.15
        for _ in range(self.n_luas):
            glTranslatef(-translate, 0, translate)

            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
            glEnable(GL_DEPTH_TEST)
            glPushMatrix()
            
            glBindTexture(GL_TEXTURE_2D, self.textura_lua) 
            glRotate(-90, 1, 0, 0)
            glRotate(angulo, 0, 0, 1)
            quadric = gluNewQuadric()
            gluQuadricTexture(quadric, GL_TRUE)
            gluSphere(quadric, 0.02, 100, 100) 
            if self.n_luas > 1:
                translate = -0.3
            glPopMatrix()


class Netuno():

    def __init__(self, textura, textura_lua, n_luas):
        self.textura = textura
        self.textura_lua = textura_lua
        self.n_luas = n_luas

    def desenha(self, angulo):
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(-3.2, 0, 3.2)
        glBindTexture(GL_TEXTURE_2D, self.textura) 
        glRotate(-90, 1, 0, 0)
        glRotate(angulo, 0, 0, 1)
        quadric = gluNewQuadric()
        gluQuadricTexture(quadric, GL_TRUE)
        gluSphere(quadric, 0.11, 100, 100) 
        self.desenha_lua(angulo)
        glPopMatrix()


    def orbita(self):
        radius, num_segments, height = 4.5, 100, 0
        glBegin(GL_LINE_LOOP)
        for i in range(num_segments):
            theta = 2.0 * 3.1415926 * i / num_segments
            x = radius * cos(theta)
            y = radius * sin(theta)
            glVertex3f(x, y, height)
        glEnd()

    def desenha_lua(self, angulo):
        translate = 0.2
        for _ in range(self.n_luas):
            glTranslatef(-translate, 0, translate)

            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
            glEnable(GL_DEPTH_TEST)
            glPushMatrix()
            glBindTexture(GL_TEXTURE_2D, self.textura_lua) 
            glRotate(-90, 1, 0, 0)
            glRotate(angulo, 0, 0, 1)
            quadric = gluNewQuadric()
            gluQuadricTexture(quadric, GL_TRUE)
            gluSphere(quadric, 0.02, 100, 100) 
            if self.n_luas > 1:
                translate = -0.4
            glPopMatrix()