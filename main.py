import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from planetas import * 

pygame.init()
display = (1500, 720)
win = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Inicializar a matriz de projeção
glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)

#CARREGA TEXTURAS DO FUNDO
TEXTURA_FUNDO_ID = "texturas/fundo.jpg"
TEXTURA_FUNDO = load_texture(TEXTURA_FUNDO_ID)

#CARREGA TEXTURAS DO SOL
TEXTURA_SOL_ID = "texturas/sol.jpg"
TEXTURA_SOL = load_texture(TEXTURA_SOL_ID)

TEXTURA_MERCURIO_ID = "texturas/mercurio.jpg"
TEXTURA_MERCURIO = load_texture(TEXTURA_MERCURIO_ID)

TEXTURA_VENUS_ID = "texturas/venus2.jpg"
TEXTURA_VENUS = load_texture(TEXTURA_VENUS_ID)

TEXTURA_TERRA_ID = "texturas/terra.jpg"
TEXTURA_TERRA = load_texture(TEXTURA_TERRA_ID)

TEXTURA_MARTE_ID = "texturas/marte.jpg"
TEXTURA_MARTE = load_texture(TEXTURA_MARTE_ID)

TEXTURA_JUPITER_ID = "texturas/jupiter.jpg"
TEXTURA_JUPITER = load_texture(TEXTURA_JUPITER_ID)

TEXTURA_SATURNO_ID = "texturas/saturno.jpg"
TEXTURA_SATURNO = load_texture(TEXTURA_SATURNO_ID)

TEXTURA_SATURNO_ANEIS = "texturas/aneis_saturno.png"
TEXTURA_SATURNO_ANEIS = load_texture(TEXTURA_SATURNO_ANEIS)

TEXTURA_URANO_ID = "texturas/uranu.jpg"
TEXTURA_URANO = load_texture(TEXTURA_URANO_ID)

TEXTURA_NETUNO_ID = "texturas/netuno.jpg"
TEXTURA_NETUNO = load_texture(TEXTURA_NETUNO_ID)

#instancia as classes
fundo = Fundo(TEXTURA_FUNDO)
sol = Sol(TEXTURA_SOL)
mercurio = Mercurio(TEXTURA_MERCURIO)
venus = Venus(TEXTURA_VENUS)
terra = Terra(TEXTURA_TERRA)
marte = Marte(TEXTURA_MARTE)
jupiter = Jupiter(TEXTURA_JUPITER)
saturno = Saturno(TEXTURA_SATURNO, TEXTURA_SATURNO_ANEIS)
urano = Urano(TEXTURA_URANO)
netuno = Netuno(TEXTURA_NETUNO)

angulo = 0
anguloMercurio = 0
anguloVenus = 0
anguloTerra = 0
anguloVenus = 0
anguloMarte = 0
anguloJupiter = 0
anguloSaturno = 0
anguloUrano = 0
anguloNetuno = 0

def desenha_orbitas():
    #orbita mercurio

    glPushMatrix()
    glColor3f(0.8, 0.8, 0.8)
    glRotate(-90, 1, 0, 0)
    mercurio.orbita()
    glPopMatrix()

    # #orbita venus
    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)  

    glRotate(-90, 1, 0, 0)
    venus.orbita()
    glPopMatrix()

    #orbita terra
    glPushMatrix()
    glColor3f(0, 0.1, 1.0)  
    glRotate(-90, 1, 0, 0)
    terra.orbita()
    glPopMatrix()

    # #orbita marte
    glPushMatrix()
    glColor3f(1.0, 0.5, 0.5) 
    glRotate(-90, 1, 0, 0)
    marte.orbita()
    glPopMatrix()

    #orbita jupiter
    glPushMatrix()
    glColor3f(1.0, 0.8, 0.8)
    glRotate(-90, 1, 0, 0)
    jupiter.orbita()
    glPopMatrix()

    #orbita saturno
    glPushMatrix()
    glColor3f(1.0, 0.8, 0.8) 
    glRotate(-90, 1, 0, 0)
    saturno.orbita()
    glPopMatrix()

    #orbita urano
    glPushMatrix()
    glColor3f(0.0, 0.8, 1)
    glRotate(-90, 1, 0, 0)
    urano.orbita()
    glPopMatrix()

    #orbita netuno
    glPushMatrix()
    glColor3f(0, 0, 1)
    glRotate(-90, 1, 0, 0)
    netuno.orbita()
    glPopMatrix()

camera_x, camera_y, zoom = 0, 0, 1
rotatex, rotatey, rotatez = 0, 0, 0

glTranslatef(0.0, 0.0, -8)
glRotate(10, 1, 0, 0)


glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
# Iluminação ambiente
glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.3, 0.3, 0.3, 1.0])
# Iluminação difusa
glLightfv(GL_LIGHT0, GL_DIFFUSE, [2.0, 2.0, 2.0, 1.0])
# Iluminação especular
glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
# Posição da fonte de luz
#luz no Z
glLightfv(GL_LIGHT0, GL_POSITION, [0, 0, 0, 1])


glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
glMateriali(GL_FRONT_AND_BACK, GL_SHININESS, 60)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    

        keys = pygame.key.get_pressed()

        # # Controles da câmera
        if event.type == pygame.KEYDOWN:
            # move no eixo X
            if keys[pygame.K_LEFT]:
                camera_x -= 0.01
            elif keys[pygame.K_RIGHT]:
                camera_x += 0.01
    
            # move no eixo Y
            elif keys[pygame.K_UP]:
                camera_y += 0.01
            elif keys[pygame.K_DOWN]:
                camera_y -= 0.01
            
            # rotaciona no eixo Y
            elif keys[pygame.K_w]:
                rotatey += 0.1
            elif keys[pygame.K_s]:
                rotatey -= 0.1

            # rotaciona no eixo X
            elif keys[pygame.K_a]:
                rotatez += 0.1
            elif keys[pygame.K_d]:
                rotatez -= 0.1

            elif keys[pygame.K_SPACE]:
                
                camera_x, camera_y, zoom = 0, 0, 1
                rotatex, rotatey, rotatez = 0, 0, 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            # zoom
            if event.button == 4:
                zoom += 0.01

            elif event.button == 5:
                zoom -= 0.01
            
            # rotaciona no eixo X
            elif event.button == 1:
                rotatex += 0.1
            
            elif event.button == 3:
                rotatex -= 0.1
            
    
    glScalef(zoom, zoom, zoom)
    glTranslatef(-camera_x, -camera_y, 0)
    # camera_x, camera_y, zoom = 0, 0, 1
    zoom = 1
    glRotate(rotatex, 1, 0, 0)
    glRotate(rotatey, 0, 1, 0)
    glRotate(rotatez, 0, 0, 1)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    fundo.desenha()

    glPushMatrix()
    glPushMatrix()
    
    
    # Configuração da iluminação
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    sol.desenha(angulo)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glPopMatrix()

    
    #mercurio
    glPushMatrix()
    glRotate(anguloMercurio, 0, 1, 0)
    mercurio.desenha(angulo)
    glPopMatrix()

   
    anguloMercurio -= 0.48
    if anguloMercurio >= 360:
        anguloMercurio = 0


    angulo -= 0.3
    if angulo >= 360:
        angulo = 0

    #venus
    glPushMatrix()
    glRotate(anguloVenus,0, 1, 0)
    venus.desenha(angulo)
    glPopMatrix()

   
    anguloVenus -= 0.35
    if anguloVenus >= 360:
        anguloVenus = 0

    #terra
    glPushMatrix()
    glRotate(anguloTerra, 0, 1, 0)
    terra.desenha(angulo)
    glPopMatrix()

   
    anguloTerra -= 0.29
    if anguloTerra >= 360:
        anguloTerra = 0

    #marte
    glPushMatrix()
    glRotate(anguloMarte, 0, 1, 0)
    marte.desenha(angulo)
    glPopMatrix()

    
    anguloMarte -= 0.24
    if anguloMarte >= 360:
        anguloMarte = 0

    #jupiter
    glPushMatrix()
    glRotate(anguloJupiter, 0, 1, 0)
    jupiter.desenha(angulo)
    glPopMatrix()


    anguloJupiter -= 0.13
    if anguloJupiter >= 360:
        anguloJupiter = 0


    #saturno
    glPushMatrix()
    glRotate(anguloSaturno, 0, 1, 0)
    saturno.desenha(angulo)
    glPopMatrix()


    anguloSaturno -= 0.096
    if anguloSaturno >= 360:
        anguloSaturno = 0


    #urano
    glPushMatrix()
    glRotate(anguloUrano, 0, 1, 0)
    urano.desenha(angulo)
    glPopMatrix()

    anguloUrano -= 0.068
    if anguloUrano >= 360:
        anguloUrano = 0

    
    #netuno
    glPushMatrix()
    glRotate(anguloNetuno, 0, 1, 0)
    netuno.desenha(angulo)
    glPopMatrix()

    anguloNetuno -= 0.054
    if anguloNetuno >= 360:
        anguloNetuno = 0

    glDisable(GL_TEXTURE_2D)

    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    desenha_orbitas()
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_TEXTURE_2D)
    glPopMatrix()
    # glDisable(GL_TEXTURE_2D)

    
    pygame.display.flip()
    pygame.time.wait(10)



