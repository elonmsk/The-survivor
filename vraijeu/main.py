import pygame
from game import Game
from player import Player
import math


#generer la fenetre du jeu
pygame.display.set_caption("THE SURVIVOR")
screen = pygame.display.set_mode((1080, 720))




#importer l'arriere plan de notre jeu
background = pygame.image.load('assets/bg.jpg')


#importer la banniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)


#importer le bouton pour lancer partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

#charger notre jeu
game = Game()

#charger notre joueur
player = Player(game)

running = True


#boucle tant que cette variable est vraie
while running:

    #appliquer la fenetre du jeu
    screen.blit(background, (0, -200))

    #verifier si le jeu a commencé ou non
    if game.is_playing:
        #declencher les instructions de la partie
        game.update(screen)
    #verifier si notre jeu n'as pas commencé
    else:
        #ajouter mon écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)


    #mettre a jour l'ecran
    pygame.display.flip()


    #si le joueeur ferme cette fenetre
    for event in pygame.event.get():

       #que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")

        #Detecter si le joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            #si la touche space est enclenche
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #VERIFICATION SI LA SOURIS EST EN COLLISION AVEC LE BUTTON
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lancé
                game.start()