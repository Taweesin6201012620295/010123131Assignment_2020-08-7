import pygame
import time
width,high = 1550,800
Green = (0,255,0)
Red = (255,0,0)
blue = (82,220,200)
display = pygame.display.set_mode([width,high],0,32)
pygame.display.set_caption("My Window")

pygame.init()
myfont = pygame.font.SysFont("Comic Sans MS",40)

def Operator(x):
    if x == "+":
        return True
    if x == "-":
        return True
    if x == "!":
        return True
    
    return False

Mot = ['&','+','+','I0','!','I1','!','I2','+','!','I0','+','I1','I2'] # (I0+!I1+!(I2))&(!I0+I1+I2) Test 3
#                                       &
#                             /                  \
#                      +                              +
#              /               \                  /       \
#            +                    !            !             +
#          /    \               /            /             /    \
#      I0        !           I2           I0             I1      I2
#              /
#            I1

run = True
while(run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Right
    pygame.draw.rect(display,blue,(800,80,400,10))
    pygame.draw.rect(display,blue,(1200,80,10,100))
    #Left
    pygame.draw.rect(display,blue,(800,80,-400,10))
    pygame.draw.rect(display,blue,(400,80,10,100))

    #Position of root       
    pygame.draw.circle(display,blue,[800,80],25)
    label = myfont.render(Mot[0],1,(255,255,255))                                          # & [0]
    display.blit(label,(790,50))

############################################################################################
# Layer 1

    #Right
    pygame.draw.rect(display,blue,(400,200,180,10))
    pygame.draw.rect(display,blue,(580,200,10,160))
    #Left
    pygame.draw.rect(display,blue,(400,200,-200,10))
    pygame.draw.rect(display,blue,(200,200,10,160))

    #Position of root L 
    pygame.draw.circle(display,blue,[400,200],25)
    label = myfont.render(Mot[1],1,(255,255,255))                                          # + [1]
    display.blit(label,(400,200))


    #Right
    pygame.draw.rect(display,blue,(1200,200,180,10))
    pygame.draw.rect(display,blue,(1380,200,10,160))
    #Left
    pygame.draw.rect(display,blue,(1200,200,-220,10))
    pygame.draw.rect(display,blue,(980,200,10,160))

    #Position of root R       
    pygame.draw.circle(display,blue,[1200,200],25)
    label = myfont.render(Mot[8],1,(255,255,255))                                          # + [8]
    display.blit(label,(1200,200))
#############################################################################################
# Layer 2

        #Right
    pygame.draw.rect(display,blue,(200,360,80,10))
    pygame.draw.rect(display,blue,(280,360,10,160))
        #Left
    pygame.draw.rect(display,blue,(200,360,-130,10))
    pygame.draw.rect(display,blue,(70,360,10,160))

        # Position Leef 1
    pygame.draw.circle(display,blue,[200,360],25)
    label = myfont.render(Mot[2],1,(255,255,255))                                         #  + [2]
    display.blit(label,(200,360))
#-------------------------------------------------------------------------    
        #Right
    pygame.draw.rect(display,blue,(580,360,100,10))
    pygame.draw.rect(display,blue,(680,360,10,160))
        #Left
    pygame.draw.rect(display,blue,(580,360,-100,10))
    pygame.draw.rect(display,blue,(480,360,10,160))

    # Position Leef 2
    pygame.draw.circle(display,blue,[580,360],25)
    label = myfont.render(Mot[6],1,(255,255,255))                                          # ! [6]
    display.blit(label,(580,360))
#--------------------------------------------------------------------------
        #Right
    pygame.draw.rect(display,blue,(980,360,100,10))
    pygame.draw.rect(display,blue,(1080,360,10,160))
        #Left
    pygame.draw.rect(display,blue,(980,360,-100,10))
    pygame.draw.rect(display,blue,(880,360,10,160))

     # Position Leef 3
    pygame.draw.circle(display,blue,[980,360],25)
    label = myfont.render(Mot[9],1,(255,255,255))                                           # ! [9]
    display.blit(label,(980,360))
#---------------------------------------------------------------------------
        #Right
    pygame.draw.rect(display,blue,(1380,360,100,10))
    pygame.draw.rect(display,blue,(1480,360,10,160))
        #Left
    pygame.draw.rect(display,blue,(1380,360,-100,10))
    pygame.draw.rect(display,blue,(1280,360,10,160))

    # Position Leef 4
    pygame.draw.circle(display,blue,[1380,360],25)
    label = myfont.render(Mot[11],1,(255,255,255))                                           # + [11]
    display.blit(label,(1380,360))
#############################################################################################
# Layer 3
    for c in range(0,(2**3)):
        A = 80+(200*c)

            #Right
        pygame.draw.rect(display,blue,(A,520,40,10))
        pygame.draw.rect(display,blue,(A+40,520,10,160)) 
            #Left
        pygame.draw.rect(display,blue,(A,520,-60,10))
        pygame.draw.rect(display,blue,(A-60,520,10,160))
        # Position Leef
        pygame.draw.circle(display,blue,[A,520],25)
        label = myfont.render(Mot[c],1,(255,255,255))
        display.blit(label,(A,520))
#############################################################################################
# Layer 4
    for d in range(0,(2**4)):
        # Position Leef 1
        B = 25+(100*d)
        pygame.draw.circle(display,blue,[B,680],25)
        label = myfont.render(Mot[5],1,(255,255,255))
        display.blit(label,(B,680))

    pygame.display.update()
    pygame.display.flip()
    
pygame.quit()