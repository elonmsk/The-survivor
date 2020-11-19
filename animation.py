import pygame


#définir class qui va s'occuper des animations

class AnimateSprite (pygame.sprite.Sprite):
    #def les choses a faire a la creation de l'entité

    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')