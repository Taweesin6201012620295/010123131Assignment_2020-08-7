import pygame
import time
width,high = 1550,800
Black = (0,0,0)
White = (255,255,255)
Green = (0,255,0)
Red = (255,0,0)
blue = (82,220,200)
Blue = (82,100,220)
display = pygame.display.set_mode([width,high],0,32)
pygame.display.set_caption("My Window")

pygame.init()
myfont = pygame.font.SysFont("Comic Sans MS",30)

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
    pygame.draw.rect(display,Blue,(800,80,400,10))
    pygame.draw.rect(display,Blue,(1200,80,10,100))
    #Left
    pygame.draw.rect(display,Blue,(800,80,-400,10))
    pygame.draw.rect(display,Blue,(400,80,10,100))

    #Position of root       
    pygame.draw.circle(display,blue,[800,80],25)
    label = myfont.render(Mot[0],1,(Black))                                          # & [0]
    display.blit(label,(790,50))

############################################################################################
# Layer 1

    #Right
    pygame.draw.rect(display,Blue,(400,200,180,10))
    pygame.draw.rect(display,Blue,(580,200,10,160))
    #Left
    pygame.draw.rect(display,Blue,(400,200,-200,10))
    pygame.draw.rect(display,Blue,(200,200,10,160))

    #Position of root L 
    pygame.draw.circle(display,blue,[400,200],25)
    label = myfont.render(Mot[1],1,(Black))                                          # + [1]
    display.blit(label,(390,180))


    #Right
    pygame.draw.rect(display,Blue,(1200,200,180,10))
    pygame.draw.rect(display,Blue,(1380,200,10,160))
    #Left
    pygame.draw.rect(display,Blue,(1200,200,-220,10))
    pygame.draw.rect(display,Blue,(980,200,10,160))

    #Position of root R       
    pygame.draw.circle(display,blue,[1200,200],25)
    label = myfont.render(Mot[8],1,(Black))                                          # + [8]
    display.blit(label,(1190,180))
#############################################################################################
# Layer 2

        #Right
    pygame.draw.rect(display,Blue,(200,360,80,10))
    pygame.draw.rect(display,Blue,(280,360,10,160))
        #Left
    pygame.draw.rect(display,Blue,(200,360,-130,10))
    pygame.draw.rect(display,Blue,(70,360,10,160))

        # Position Leef 1
    pygame.draw.circle(display,blue,[200,360],25)
    label = myfont.render(Mot[2],1,(Black))                                         #  + [2]
    display.blit(label,(190,340))
#-------------------------------------------------------------------------    
        #Right
    pygame.draw.rect(display,Blue,(580,360,100,10))
    pygame.draw.rect(display,Blue,(680,360,10,160))
        #Left
    pygame.draw.rect(display,Blue,(580,360,-100,10))
    pygame.draw.rect(display,Blue,(480,360,10,160))

    # Position Leef 2
    pygame.draw.circle(display,blue,[580,360],25)
    label = myfont.render(Mot[6],1,(Black))                                          # ! [6]
    display.blit(label,(570,340))
#--------------------------------------------------------------------------
        #Right
    pygame.draw.rect(display,Blue,(980,360,100,10))
    pygame.draw.rect(display,Blue,(1080,360,10,160))
        #Left
    pygame.draw.rect(display,Blue,(980,360,-100,10))
    pygame.draw.rect(display,Blue,(880,360,10,160))

     # Position Leef 3
    pygame.draw.circle(display,blue,[980,360],25)
    label = myfont.render(Mot[9],1,(Black))                                           # ! [9]
    display.blit(label,(970,340))
#---------------------------------------------------------------------------
        #Right
    pygame.draw.rect(display,Blue,(1380,360,100,10))
    pygame.draw.rect(display,Blue,(1480,360,10,160))
        #Left
    pygame.draw.rect(display,Blue,(1380,360,-100,10))
    pygame.draw.rect(display,Blue,(1280,360,10,160))

    # Position Leef 4
    pygame.draw.circle(display,blue,[1380,360],25)
    label = myfont.render(Mot[11],1,(Black))                                           # + [11]
    display.blit(label,(1370,340))
#############################################################################################
# Layer 3
    for c in range(0,(2**3)):
        A = 80+(200*c)

            #Right
        pygame.draw.rect(display,Blue,(A,520,40,10))
        pygame.draw.rect(display,Blue,(A+40,520,10,160)) 
            #Left
        pygame.draw.rect(display,Blue,(A,520,-60,10))
        pygame.draw.rect(display,Blue,(A-60,520,10,160))
        # Position Leef
        pygame.draw.circle(display,blue,[A,520],25)

    # Text 1 
    label = myfont.render(Mot[3],1,(Black))                # I0 [3]
    display.blit(label,(60,500))
    # Text 2
    label = myfont.render(Mot[4],1,(Black))                # ! [4]
    display.blit(label,(260,500))
    # Text 3
    label = myfont.render(Mot[7],1,(Black))                # I2 [7]
    display.blit(label,(460,500))
    # Text 4
    label = myfont.render("N",1,(Black))               # None 
    display.blit(label,(660,500))
    # Text 5
    label = myfont.render(Mot[10],1,(Black))               # I0  [10]
    display.blit(label,(860,500))
    # Text 6
    label = myfont.render("N",1,(Black))               # None
    display.blit(label,(1060,500))
    # Text 7
    label = myfont.render(Mot[12],1,(Black))              # I1  [12]
    display.blit(label,(1260,500))
    # Text 8
    label = myfont.render(Mot[13],1,(Black))              # I2   [13]
    display.blit(label,(1460,500))
#############################################################################################
# Layer 4
    for d in range(0,(2**4)):
        # Position Leef 1
        B = 25+(100*d)
        pygame.draw.circle(display,blue,[B,680],25)
        #label = myfont.render("N",1,(Black))
        #display.blit(label,(B-20,660))

    label = myfont.render(Mot[5],1,(Black))             # I1 [5]
    display.blit(label,(205,660))

    pygame.display.update()
    pygame.display.flip()
    
pygame.quit()