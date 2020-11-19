import pygame


#définir class qui va s'occuper des animations

class AnimateSprite (pygame.sprite.Sprite):
    #def les choses a faire a la creation de l'entité

    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0  #commencer l'anim à l'image 0
        self.images = animation.get(sprite_name)


    #definir une methode pour annimer le sprite
    def animate(self):

        #passser a l'image suivante
        self.current_image += 1

        #verifier si on a atteint la fin de l'animation
        if self.current_image >=len(self.images):
            #remettre l'image au depart
            self.current_image = 0

        #modifeier l'image precedente par la suivante
        self.image = self.images[self.current_image]


#definir une fonction pour charger les images d'un sprite

def load_animation_image(sprite_name):

    #charger les 24 images de ce sprite dans le dossier correspondant

    images = []

    #recuperer le chemin du dossier pour ce sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    #boucler sur chaque image dans ce dossier
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    #renvoyer la liste d'image
    return images

#definir un dictionnaire qui va contenir les images chargées de chaque sprite
#mummy -> [...mummy1.png, ...mummy2.png, ...]


animations = {
    "mummy": load_animation_image("mummy")
}
