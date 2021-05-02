# -*- coding: latin-1 -*-
import pygame
pygame.init()

pygame.display.set_caption("Ma rencontre avec un robot sur Mars")
ecran=pygame.display.set_mode((1000,630))

pygame.event.get()

#image d'arrière-plan
fond=pygame.image.load('image/arriere-plan2.png')

#personnage
perso=pygame.image.load('image/test.png')
perso=pygame.transform.scale(perso, (300, 285))
robot=pygame.image.load('image/robot.png')
robot=pygame.transform.scale(robot, (350, 245))
cle=pygame.image.load('image/cle.png')
cle=pygame.transform.scale(cle, (70, 55))

#animation d'introduction
for i in range(8):
    ecran.blit(fond,(0,0))
    ecran.blit(perso,(20*i,250))
    ecran.blit(robot,(400,280))
    pygame.display.flip()
    pygame.time.wait(20)

#code nécessaire pour écrire du texte à l'écran
font=pygame.font.SysFont(None,30)


def ligne_de_texte(texte):
    return font.render(texte, False, (0, 0, 0))
x_texte_perso=170
y_texte_perso=200
espace_vertical=40

x_texte_robot=420
y_texte_robot=200
espace_vertical=40

#Texte personnage
perso_texte=[]
perso_texte.append(ligne_de_texte("Ouah...!!!! Mais qui est tu ?"))
perso_texte.append(ligne_de_texte("Que t'est-il arrivé ?"))
perso_texte.append(ligne_de_texte("tu veux que je t'aide ?"))

#Texte robot
robot_texte=[]
robot_texte.append(ligne_de_texte("Je suis un robot venu de Mars"))
robot_texte.append(ligne_de_texte("J'ai eu une panne de carburant, je viens de m'écraser"))
robot_texte.append(ligne_de_texte("oh oui ca me ferais plaisir !"))

#affichage du message
ecran.blit(perso_texte[0],(x_texte_perso,y_texte_perso))
pygame.display.flip()

#on affiche le fond et le personnage
ecran.blit(fond,(0,0))
ecran.blit(perso,(140,250))
ecran.blit(robot,(400,280))



pygame.time.wait(3000)
ecran.blit(perso_texte[1],(x_texte_perso,y_texte_perso))
pygame.display.flip()

#on affiche le fond et le personnage
ecran.blit(fond,(0,0))
ecran.blit(perso,(140,250))
ecran.blit(robot,(400,280))

#pause de 1 seconde
pygame.time.wait(3000)


ecran.blit(robot_texte[0],(x_texte_robot,y_texte_robot))
pygame.display.flip()
#on affiche le fond et le personnage
ecran.blit(fond,(0,0))
ecran.blit(perso,(140,250))
ecran.blit(robot,(400,280))

#pause de 1 seconde
pygame.time.wait(3000)

ecran.blit(robot_texte[1],(330,200))
pygame.display.flip()
#on affiche le fond et le personnage
ecran.blit(fond,(0,0))
ecran.blit(perso,(140,250))
ecran.blit(robot,(400,280))

#pause de 1 seconde
pygame.time.wait(3000)

ecran.blit(perso_texte[2],(x_texte_perso,y_texte_perso))
pygame.display.flip()
#on affiche le fond et le personnage
ecran.blit(fond,(0,0))
ecran.blit(perso,(140,250))
ecran.blit(robot,(400,280))

#pause de 1 seconde
pygame.time.wait(3000)

ecran.blit(robot_texte[2],(x_texte_robot,y_texte_robot))
pygame.display.flip()
#on affiche le fond et le personnage
ecran.blit(fond,(0,0))
ecran.blit(perso,(140,250))
ecran.blit(robot,(400,280))

#pause de 1 seconde
pygame.time.wait(3000)


#animation de fin
for i in range(15):
    ecran.blit(fond,(0,0))
    ecran.blit(perso,(20*i,250))
    ecran.blit(robot,(400,280))
    pygame.display.flip()
    pygame.time.wait(20)

    # on affiche le fond et le personnage
    ecran.blit(fond, (0, 0))
    ecran.blit(perso, (300, 250))
    ecran.blit(robot, (400, 280))
    ecran.blit(cle, (300, 390))



#boucle principale
continuer = True
question_actuelle=0
score=0
while continuer:
    #on affiche le fond et le personnage
    ecran.blit(fond,(0,0))
    ecran.blit(perso,(300,250))
    ecran.blit(robot,(400,280))
    ecran.blit(cle, (470, 400))
    


    pygame.display.flip()

    #gestion des événements
    for event in pygame.event.get():
        #Le joueur a fermé la fenêtre
        if event.type == pygame.QUIT:
            continuer = False
            pygame.quit()
      