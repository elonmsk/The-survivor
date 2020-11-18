import pygame
import random

#creer une classe pour gérer cette comete
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        #definir l image associer a la comete
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(7, 9)
        self.rect.x = random.randint(20, 900)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        # Verifier si le nombre de comettes est de 0
        if len(self.comet_event.all_comets) == 0:
            print("l'evenement est fini")
            #remettre la barre a 0
            self.comet_event.reset_percent()
            #apparaitre les 2 premiers monstre
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()
    def fall(self):
        self.rect.y += self.velocity


        #ne tombe pas sur le sol
        if self.rect.y >+ 500:
            print("sol")
            #retirer la boule de feu
            self.comet_event.all_comets.remove(self)
            #verifier si il n'y a plus de boule de feu
            if len(self.comet_event.all_comets) == 0:
                print("l'evenement est fini")
                #remettre la jauge au depart
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        #verifier si la boule de feu touche le joeur
        if self.comet_event.game.check_collision(
                self, self.comet_event.game.all_players
        ):
            print("jouer touché")
            #retirer la boule de feu
            self.remove()
            #subir des degats 20 point de vie
            self.comet_event.game.player.damage(20)
