import pygame
from map import Map
from constantes import *
from affichage import afficher_carte

carte = Map(
    niveau_1_largeur,
    niveau_1_hauteur,
    niveau_1_chemins,
    niveau_1_decor,
    niveau_1_unites,
)

pygame.display.init()
fenetre = pygame.display.set_mode((carte.width, carte.height))

afficher_carte(carte, fenetre)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    afficher_carte(carte, fenetre)

pygame.quit()
