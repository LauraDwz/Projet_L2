import logging

logging.basicConfig(
    filename="mon_jeu.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
import pygame
from src.model.map import Map
from src.utils.constantes import *
from src.view.affichage import afficher_carte

carte = Map("../../assets/levels/level1.txt")

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
