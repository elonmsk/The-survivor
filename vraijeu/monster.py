import pygame
import random
import animation

# créer une classe qui gère la notion de monstre sur le jeu

class Monster(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("mummy")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 3)

    def damage(self, amount):
        # infliger des degats
        self.health -= amount

        # verifier si son nouveau nombre de point de vie est inférieur ou égale à 0
        if self.health <= 0:
            # Réapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health

            # si la barre d'evenement est chargé au max
            if self.game.comet_event.is_full_loaded():
                # retirer du jeu
                self.game.all_monsters.remove(self)

                # appel de la methode pour essayer de declencher pluie de comete
                self.game.comet_event.attempt_fall()

    def update_health_bar(self, surface):
        # dessiner la barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        # le deplacement ne se fait si il n'y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le joueur
        else:
            # infliger des degtas au joueur
            self.game.player.damage(self.attack)
