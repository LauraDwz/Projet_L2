from src.utils.constantes import COTE_CASE
import pygame


def afficher_carte(carte, surface):
    for box in carte.path_boxes:
        image = pygame.transform.scale(
            pygame.image.load(box.image), (COTE_CASE, COTE_CASE)
        )
        surface.blit(
            image,
            (box.x * COTE_CASE, box.y * COTE_CASE),
        )
    for box in carte.decor_boxes:
        image = pygame.transform.scale(
            pygame.image.load(box.image), (COTE_CASE, COTE_CASE)
        )
        surface.blit(
            image,
            (box.x * COTE_CASE, box.y * COTE_CASE),
        )
    for box in carte.unit_boxes:
        image = pygame.transform.scale(
            pygame.image.load(box.image), (COTE_CASE, COTE_CASE)
        )
        surface.blit(
            image,
            (box.x * COTE_CASE, box.y * COTE_CASE),
        )
