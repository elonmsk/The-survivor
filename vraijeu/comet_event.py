import pygame
from comet import Comet


#créer une classe pour gérer cet evenement
class CometFallEvent:

    #lors du chargement => creer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 35
        self.game = game
        self.fall_mode = True


        #definir un groupe de sprite pour stocker les cometes
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100


    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0


    def meteor_fall(self):
        for i in range (3,10):
            self.all_comets.add(Comet(self))


    def attempt_fall(self):
        #la jauge d evenement est chargée
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("Pluie de cométe !!")
            self.meteor_fall()
            self.reset_percent()
            self.fall_mode = True #activer l'evenement



    def update_bar(self, surface):

        #ajouter du pourcentage à la bar
        self.add_percent()

        #appel de la methode pour essayer de declencher pluie de comete
        self.attempt_fall()



        # barre noir(arriere plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0, #axe des x
            surface.get_height() - 20, #axe des y
            (surface.get_width() / 100), # longueur de la fenetre
            10  # épaisseur de la barre
        ])
        #barre rouge (jauge d'event)
        pygame.draw.rect(surface, (18, 11, 11), [
            0,  # axe des x
            surface.get_height() - 20,  # axe des y
            (surface.get_width() / 100) * self.percent,  # longueur de la fenetre
            10  # épaisseur de la barre
        ])

