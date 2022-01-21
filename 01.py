import pygame
import os
import sys

WINDOW_SIZE = W_WIDTH, W_HEIGHT = 800, 600


def draw(screen):
    font = pygame.font.Font(None, 50)
    text = font.render("Press 'z' to start game!", True, (100, 255, 100))
    text2 = font.render("Press 'q' to finish game", True, (100, 255, 100))
    screen.blit(text, (200, 106))
    screen.blit(text2, (200, 450))
    pygame.draw.rect(screen, (0, 255, 0), (190, 90, 391, 60), 1)
    pygame.draw.rect(screen, (0, 255, 0), (190, 440, 401, 60), 1)


def main_menu():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)

    screen.fill((100, 100, 100))
    draw(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    game_menu()
                if event.key == pygame.K_q:
                    running = False

        pygame.display.flip()
    pygame.quit()


def game_menu():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)

    screen.fill((100, 100, 100))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    main_menu()
                if event.key == pygame.K_q:
                    running = False

        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main_menu()