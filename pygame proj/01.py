import pygame

pygame.init()

screen = pygame.display.set_mode((500, 300))

pacman = pygame.image.load('pm.png')

pmX = 0
pmY = 200
speed = 10

to_left = False
to_right = False
to_up = False
to_down = False

while True:

    screen.fill(("black"))

    pygame.time.delay(30)

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                to_left = True

            if event.key == pygame.K_RIGHT:
                to_right = True

            if event.key == pygame.K_DOWN:
                to_down = True

            if event.key == pygame.K_UP:
                to_up = True

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                to_left = False

            if event.key == pygame.K_RIGHT:
                to_right = False

            if event.key == pygame.K_DOWN:
                to_down = False

            if event.key == pygame.K_UP:
                to_up = False

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if to_right:
        pmX += speed
    if to_left:
        pmX -= speed
    if to_down:
        pmY += speed
    if to_up:
        pmY -= speed

    screen.blit(pacman, (pmX, pmY))
    pygame.display.update()

