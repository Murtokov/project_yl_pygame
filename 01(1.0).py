import pygame
import os
import sys
import random

FPS = 70

WINDOW_SIZE = W_WIDTH, W_HEIGHT = 800, 600
global gh_c_n
collected_coins = 0
coins = 0
lang = 'eng'
can_w = 1


def draw(screen):
    font = pygame.font.Font(None, 50)
    font2 = pygame.font.Font(None, 25)
    if lang == 'eng':
        text = font.render("Press 'z' to start game!", True, (100, 255, 100))
        text2 = font.render("Press 'q' to finish game", True, (100, 255, 100))
        text3 = font.render("Press 'i' to see rules", True, (100, 255, 100))
        text4 = font.render("Press 'j' to see the leaderboard", True, (100, 255, 100))
        text5 = font2.render("ENG to RUS", True, (100, 255, 100))
        screen.blit(text, (200, 106))
        screen.blit(text2, (200, 406))
        screen.blit(text3, (200, 206))
        screen.blit(text4, (200, 306))
        screen.blit(text5, (50, 550))
        pygame.draw.rect(screen, (0, 255, 0), (190, 90, 391, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (190, 390, 401, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (190, 190, 351, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (190, 290, 531, 60), 1)
    else:
        text = font.render("Нажмите 'z' для начала игры!", True, (100, 255, 100))
        text2 = font.render("Нажмите 'q' чтобы закончить", True, (100, 255, 100))
        text3 = font.render("Нажмите 'i' для показа правил", True, (100, 255, 100))
        text4 = font.render("Нажмите 'j' для показа лидеров", True, (100, 255, 100))
        text5 = font2.render("РУС в АНГ", True, (100, 255, 100))
        screen.blit(text, (200, 106))
        screen.blit(text2, (200, 406))
        screen.blit(text3, (200, 206))
        screen.blit(text4, (200, 306))
        screen.blit(text5, (50, 550))
        pygame.draw.rect(screen, (0, 255, 0), (190, 90, 531, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (190, 390, 511, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (190, 190, 546, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (190, 290, 566, 60), 1)


def draw2(screen):
    if lang == 'eng':
        font = pygame.font.Font(None, 50)
        text = font.render("left up right down to move", True, (100, 255, 100))
        text2 = font.render("Collect all coins to win", True, (100, 255, 100))
        text3 = font.render("Ghosts can catch you", True, (100, 255, 100))
        text4 = font.render("Press 'z' to return", True, (100, 255, 100))
        screen.blit(text, (100, 106))
        screen.blit(text2, (100, 306))
        screen.blit(text3, (100, 206))
        screen.blit(text4, (100, 406))
        pygame.draw.rect(screen, (0, 255, 0), (90, 90, 451, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (90, 290, 396, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (90, 190, 381, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (90, 390, 311, 60), 1)
    else:
        font = pygame.font.Font(None, 50)
        text = font.render("left up right down чтобы двигаться", True, (100, 255, 100))
        text2 = font.render("Для победы нужно собрать все монеты", True, (100, 255, 100))
        text3 = font.render("Призраки могут поймать Вас", True, (100, 255, 100))
        text4 = font.render("Нажмите 'z' чтобы вернуться", True, (100, 255, 100))
        screen.blit(text, (100, 106))
        screen.blit(text2, (100, 306))
        screen.blit(text3, (100, 206))
        screen.blit(text4, (100, 406))
        pygame.draw.rect(screen, (0, 255, 0), (90, 90, 611, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (90, 290, 701, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (90, 190, 511, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (90, 390, 511, 60), 1)


def draw3(screen):
    if lang == 'eng':
        font = pygame.font.Font(None, 50)
        text = font.render("Yow win!", True, (100, 255, 100))
        text2 = font.render("Your score:", True, (100, 255, 100))
        text3 = font.render(str(collected_coins), True, (100, 255, 100))
        text4 = font.render("Press 'n' to save the result", True, (100, 255, 100))
        screen.blit(text, (100, 106))
        screen.blit(text3, (100, 306))
        screen.blit(text2, (100, 206))
        screen.blit(text4, (100, 406))
        pygame.draw.rect(screen, (0, 255, 0), (90, 90, 176, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (90, 290, 211, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (90, 190, 211, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (90, 390, 451, 60), 1)
    else:
        font = pygame.font.Font(None, 50)
        text = font.render("Вы выиграли!", True, (100, 255, 100))
        text2 = font.render("Ваш счёт:", True, (100, 255, 100))
        text3 = font.render(str(collected_coins), True, (100, 255, 100))
        text4 = font.render("Нажмите 'n' чтобы закрепить результат", True, (100, 255, 100))
        screen.blit(text, (100, 106))
        screen.blit(text3, (100, 306))
        screen.blit(text2, (100, 206))
        screen.blit(text4, (100, 406))
        pygame.draw.rect(screen, (0, 255, 0), (90, 90, 261, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (90, 290, 191, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (90, 190, 191, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (90, 390, 686, 60), 1)


def draw4(screen):
    if lang == 'eng':
        font = pygame.font.Font(None, 50)
        text = font.render("Game Over!", True, (100, 255, 100))
        text2 = font.render("Your score:", True, (100, 255, 100))
        text3 = font.render(str(collected_coins), True, (100, 255, 100))
        text4 = font.render("Press 'n' to save the result", True, (100, 255, 100))
        screen.blit(text, (100, 106))
        screen.blit(text3, (100, 306))
        screen.blit(text2, (100, 206))
        screen.blit(text4, (100, 406))
        pygame.draw.rect(screen, (0, 255, 0), (90, 90, 216, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (90, 290, 211, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (90, 190, 211, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (90, 390, 451, 60), 1)
    else:
        font = pygame.font.Font(None, 50)
        text = font.render("Игра окончена!", True, (100, 255, 100))
        text2 = font.render("Ваш счёт:", True, (100, 255, 100))
        text3 = font.render(str(collected_coins), True, (100, 255, 100))
        text4 = font.render("Нажмите 'n' чтобы закрепить результат", True, (100, 255, 100))
        screen.blit(text, (100, 106))
        screen.blit(text3, (100, 306))
        screen.blit(text2, (100, 206))
        screen.blit(text4, (100, 406))
        pygame.draw.rect(screen, (0, 255, 0), (90, 90, 281, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (90, 290, 191, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (90, 190, 191, 60), 1)
        pygame.draw.rect(screen, (0, 255, 0), (90, 390, 686, 60), 1)


def draw5(screen):
    f = open('leaders.txt', 'r')
    data = list()
    for i in f.read().split('\n'):
        if i != '':
            data.append(i.split(';'))
    if data[-1][0] != 'player':
        data = data[1:]
        data.sort(key=lambda x: int(x[1]), reverse=True)
    else:
        data = data[1:]
        if lang == 'eng':
            nr = 'no results'
        else:
            nr = 'нет результатов'
    f.close()
    if lang == 'eng':
        font = pygame.font.Font(None, 65)
        font2 = pygame.font.Font(None, 65)
        text = font.render("Best score:", True, (100, 255, 100))
        screen.blit(text, (270, 106))
        if len(data) >= 1:
            text2 = font2.render('1' + ' - ' + str(data[0][1]), True, (100, 255, 100))
            screen.blit(text2, (335, 206))
        else:
            nr = 'no results'
            text2 = font.render(nr, True, (100, 255, 100))
            screen.blit(text2, (275, 206))
        if len(data) >= 2:
            text3 = font2.render('2' + ' - ' + str(data[1][1]), True, (100, 255, 100))
            screen.blit(text3, (335, 266))
        if len(data) >= 3:
            text4 = font2.render('3' + ' - ' + str(data[1][1]), True, (100, 255, 100))
            screen.blit(text4, (335, 336))
        if len(data) >= 4:
            text5 = font2.render('4' + ' - ' + str(data[1][1]), True, (100, 255, 100))
            screen.blit(text5, (335, 396))
        if len(data) >= 5:
            text6 = font2.render('5' + ' - ' + str(data[1][1]), True, (100, 255, 100))
            screen.blit(text6, (335, 456))
        pygame.draw.rect(screen, (0, 255, 0), (260, 95, 256, 60), 1)
    else:
        font = pygame.font.Font(None, 65)
        font2 = pygame.font.Font(None, 65)
        text = font2.render("Лучшие результаты:", True, (100, 255, 100))
        screen.blit(text, (180, 106))
        if len(data) >= 1:
            text2 = font2.render('1' + ' - ' + str(data[0][1]), True, (100, 255, 100))
            screen.blit(text2, (335, 206))
        else:
            nr = 'нет результатов'
            text2 = font.render(nr, True, (100, 255, 100))
            screen.blit(text2, (215, 206))
        if len(data) >= 2:
            text3 = font2.render('2' + ' - ' + str(data[1][1]), True, (100, 255, 100))
            screen.blit(text3, (335, 266))
        if len(data) >= 3:
            text4 = font2.render('3' + ' - ' + str(data[1][1]), True, (100, 255, 100))
            screen.blit(text4, (335, 336))
        if len(data) >= 4:
            text5 = font2.render('4' + ' - ' + str(data[1][1]), True, (100, 255, 100))
            screen.blit(text5, (335, 396))
        if len(data) >= 5:
            text6 = font2.render('5' + ' - ' + str(data[1][1]), True, (100, 255, 100))
            screen.blit(text6, (335, 456))
        pygame.draw.rect(screen, (0, 255, 0), (170, 95, 471, 60), 1)


def load_images(path):
    images = []
    for file_name in os.listdir(path):
        image = pygame.image.load(path + os.sep + file_name).convert_alpha()
        images.append(image)
    return images


all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
ghost_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()
all_sprites_pl = pygame.sprite.Group()


class AnimatedSprite(pygame.sprite.Sprite):

    def __init__(self, position, images):
        self.x = 0
        self.y = 1

        super(AnimatedSprite, self).__init__()

        size = (35, 35)

        self.can_move_x = 0
        self.can_move_y = 0

        self.rect = pygame.Rect(position, size)
        self.images = images
        self.images_right = images
        self.images_left = [pygame.transform.flip(image, True, False) for image in images]
        self.images_up = [pygame.transform.rotate(image, 90) for image in images]
        self.images_down = [pygame.transform.rotate(image, -90) for image in images]

        self.index = 0
        self.image = images[self.index]

        self.velocity = pygame.math.Vector2(0, 0)

        self.animation_time = 0.1
        self.current_time = 0

        self.animation_frames = 6
        self.current_frame = 0

    def update_time_dependent(self, dt):

        if self.velocity.x > 0:
            self.images = self.images_right
        elif self.velocity.x < 0:
            self.images = self.images_left
        elif self.velocity.y < 0:
            self.images = self.images_up
        elif self.velocity.y > 0:
            self.images = self.images_down

        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(*self.velocity)

    def update(self, dt):
        self.update_time_dependent(dt)

        if pygame.sprite.spritecollideany(self, vertical_borders):
            if self.velocity.x > 0:
                self.can_move_x = 1
                self.rect.x -= 10
            if self.velocity.x < 0:
                self.can_move_x = -1
                self.rect.x += 10
            self.velocity.x = 0
        else:
            self.can_move_x = 0

        if pygame.sprite.spritecollideany(self, horizontal_borders):
            if self.velocity.y > 0:
                self.can_move_y = 1
                self.rect.y -= 10
            if self.velocity.y < 0:
                self.can_move_y = -1
                self.rect.y += 10
            self.velocity.y = 0
        else:
            self.can_move_y = 0

        if pygame.sprite.spritecollideany(self, ghost_sprites):
            lose_menu()


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


class Border2(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([30, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 30, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 30])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 30)


class Coin(pygame.sprite.Sprite):
    image = pygame.transform.scale(pygame.image.load(os.path.join('images', f'coin.png')), (20, 20))
    image2 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'coin.png')), (0, 0))

    def __init__(self, group, coord):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(group)
        super().__init__(all_sprites)
        self.is_active = 1
        self.image = Coin.image
        self.rect = self.image.get_rect()
        self.rect.y = coord[0]
        self.rect.x = coord[1]
        self.add(coin_sprites)

    def update(self, *args):
        global collected_coins
        global coins
        if pygame.sprite.spritecollideany(self, all_sprites_pl):
            self.image = Coin.image2
            self.remove(coin_sprites)
            if self.is_active == 1:
                collected_coins += 1
                self.is_active = 0
                coins -= 1


class Ghost(pygame.sprite.Sprite):
    ghost1_r_1 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_1_1_1.png')), (40, 40))
    ghost1_r_2 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_1_1_2.png')), (40, 40))
    ghost1_r_3 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_1_2_1.png')), (40, 40))
    ghost1_r_4 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_1_2_2.png')), (40, 40))
    ghost1_r_5 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_1_3_1.png')), (40, 40))
    ghost1_r_6 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_1_3_2.png')), (40, 40))
    ghost1_r_7 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_1_4_1.png')), (40, 40))
    ghost1_r_8 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_1_4_2.png')), (40, 40))

    ghost2_r_1 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_2_1_1.png')), (40, 40))
    ghost2_r_2 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_2_1_2.png')), (40, 40))
    ghost2_r_3 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_2_2_1.png')), (40, 40))
    ghost2_r_4 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_2_2_2.png')), (40, 40))
    ghost2_r_5 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_2_3_1.png')), (40, 40))
    ghost2_r_6 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_2_3_2.png')), (40, 40))
    ghost2_r_7 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_2_4_1.png')), (40, 40))
    ghost2_r_8 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_2_4_2.png')), (40, 40))

    ghost3_r_1 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_3_1_1.png')), (40, 40))
    ghost3_r_2 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_3_1_2.png')), (40, 40))
    ghost3_r_3 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_3_2_1.png')), (40, 40))
    ghost3_r_4 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_3_2_2.png')), (40, 40))
    ghost3_r_5 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_3_3_1.png')), (40, 40))
    ghost3_r_6 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_3_3_2.png')), (40, 40))
    ghost3_r_7 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_3_4_1.png')), (40, 40))
    ghost3_r_8 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_3_4_2.png')), (40, 40))

    ghost4_r_1 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_4_1_1.png')), (40, 40))
    ghost4_r_2 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_4_1_2.png')), (40, 40))
    ghost4_r_3 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_4_2_1.png')), (40, 40))
    ghost4_r_4 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_4_2_2.png')), (40, 40))
    ghost4_r_5 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_4_3_1.png')), (40, 40))
    ghost4_r_6 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_4_3_2.png')), (40, 40))
    ghost4_r_7 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_4_4_1.png')), (40, 40))
    ghost4_r_8 = pygame.transform.scale(pygame.image.load(os.path.join('images', f'pacman_4_4_2.png')), (40, 40))

    def __init__(self, group, coord, img_n):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(group)
        super().__init__(all_sprites)
        self.f = 0
        self.u = 1
        self.x = 0
        self.y = 1
        self.image = Ghost.ghost2_r_1
        self.rect = self.image.get_rect()
        self.rect.y = coord[0]
        self.rect.x = coord[1]
        self.img_n = img_n
        self.add(ghost_sprites)

    def update(self, *args):
        self.f += 1
        if self.f == 5:
            if self.u == 1:
                self.u = 2
            else:
                self.u = 1
            self.f = 0
        self.remove(ghost_sprites)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.rect.y -= (5 * self.y)
            self.y = 0
            self.x = random.choice([1, -1])
        else:
            self.rect.x += (5 * self.x)
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.rect.x -= (5 * self.x)
            self.x = 0
            self.y = random.choice([1, -1])
        else:
            self.rect.y += (5 * self.y)
        self.add(ghost_sprites)
        if self.img_n == 1:
            if self.x == 1:
                if self.u == 1:
                    self.image = Ghost.ghost1_r_1
                else:
                    self.image = Ghost.ghost1_r_2
            elif self.y == 1:
                if self.u == 1:
                    self.image = Ghost.ghost1_r_3
                else:
                    self.image = Ghost.ghost1_r_4
            elif self.y == -1:
                if self.u == 1:
                    self.image = Ghost.ghost1_r_5
                else:
                    self.image = Ghost.ghost1_r_6
            elif self.x == -1:
                if self.u == 1:
                    self.image = Ghost.ghost1_r_7
                else:
                    self.image = Ghost.ghost1_r_8

        elif self.img_n == 2:
            if self.x == 1:
                if self.u == 1:
                    self.image = Ghost.ghost2_r_1
                else:
                    self.image = Ghost.ghost2_r_2
            elif self.y == 1:
                if self.u == 1:
                    self.image = Ghost.ghost2_r_3
                else:
                    self.image = Ghost.ghost2_r_4
            elif self.y == -1:
                if self.u == 1:
                    self.image = Ghost.ghost2_r_5
                else:
                    self.image = Ghost.ghost2_r_6
            elif self.x == -1:
                if self.u == 1:
                    self.image = Ghost.ghost2_r_7
                else:
                    self.image = Ghost.ghost2_r_8

        elif self.img_n == 3:
            if self.x == 1:
                if self.u == 1:
                    self.image = Ghost.ghost3_r_1
                else:
                    self.image = Ghost.ghost3_r_2
            elif self.y == 1:
                if self.u == 1:
                    self.image = Ghost.ghost3_r_3
                else:
                    self.image = Ghost.ghost3_r_4
            elif self.y == -1:
                if self.u == 1:
                    self.image = Ghost.ghost3_r_5
                else:
                    self.image = Ghost.ghost3_r_6
            elif self.x == -1:
                if self.u == 1:
                    self.image = Ghost.ghost3_r_7
                else:
                    self.image = Ghost.ghost3_r_8

        elif self.img_n == 4:
            if self.x == 1:
                if self.u == 1:
                    self.image = Ghost.ghost4_r_1
                else:
                    self.image = Ghost.ghost4_r_2
            elif self.y == 1:
                if self.u == 1:
                    self.image = Ghost.ghost4_r_3
                else:
                    self.image = Ghost.ghost4_r_4
            elif self.y == -1:
                if self.u == 1:
                    self.image = Ghost.ghost4_r_5
                else:
                    self.image = Ghost.ghost4_r_6
            elif self.x == -1:
                if self.u == 1:
                    self.image = Ghost.ghost4_r_7
                else:
                    self.image = Ghost.ghost4_r_8


def main_menu():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    global coins
    global lang

    screen.fill((100, 100, 100))
    draw(screen)

    Border(5, 5, W_WIDTH - 5, 5)
    Border(5, W_HEIGHT - 5, W_WIDTH - 5, W_HEIGHT - 5)
    Border(5, 5, 5, W_HEIGHT - 5)
    Border(W_WIDTH - 5, 5, W_WIDTH - 5, W_HEIGHT - 5)

    Border2(50, 50, 500, 50)
    Border2(50, 50, 50, 80)
    Border2(470, 50, 470, 80)

    Border2(5, 125, 600, 125)

    Border2(725, 50, 725, 230)
    Border2(725, 50, 755, 50)
    Border2(725, 200, 755, 200)

    Border2(650, 5, 650, 230)

    Border2(50, 200, 650, 200)
    Border2(50, 200, 50, 230)

    Border2(570, 50, 570, 155)
    Border2(570, 50, 600, 50)
    Border2(570, 125, 600, 125)

    Border2(725, 285, 795, 285)
    Border2(385, 550, 385, 595)
    Border2(385, 545, 725, 545)
    Border2(725, 300, 725, 575)

    Border2(150, 285, 680, 285)
    Border2(150, 285, 150, 315)

    Border2(300, 385, 500, 385)
    Border2(300, 385, 300, 415)
    Border2(470, 385, 470, 415)
    Border2(385, 470, 605, 470)
    Border2(385, 385, 385, 500)

    Border2(650, 290, 650, 500)
    Border2(650, 470, 680, 470)

    Border2(575, 380, 575, 415)
    Border2(575, 380, 605, 380)
    Border2(575, 385, 605, 385)

    Border2(225, 385, 225, 500)
    Border2(225, 385, 255, 385)
    Border2(225, 470, 330, 470)
    Border2(300, 470, 300, 545)
    Border2(300, 515, 330, 515)

    Border2(225, 545, 225, 595)
    Border2(5, 545, 255, 545)

    Border2(50, 285, 50, 500)
    Border2(50, 285, 80, 285)
    Border2(50, 470, 175, 470)
    Border2(145, 470, 145, 500)

    Border2(145, 385, 145, 430)
    Border2(145, 385, 175, 385)
    Border2(145, 400, 175, 400)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    game_menu()
                if event.key == pygame.K_i:
                    rules_menu()
                if event.key == pygame.K_j:
                    leader_menu()
                if event.key == pygame.K_q:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 140 > event.pos[0] > 45:
                    if 570 > event.pos[1] > 540:
                        if lang == 'eng':
                            lang = 'rus'
                        else:
                            lang = 'eng'
                        main_menu()

        pygame.display.flip()
    pygame.quit()


level = 2


def game_menu():
    global level
    global all_sprites_pl
    global coins
    global ghost_sprites
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)

    for ghost in ghost_sprites:
        all_sprites.remove(ghost)
    ghost_sprites = pygame.sprite.Group()

    for i in range(16):
        Coin(all_sprites, [20, 20 * (i * 2 + 1)])
        coins += 1

    for i in range(14):
        Coin(all_sprites, [95, 20 * (i * 2 + 1)])
        coins += 1

    Coin(all_sprites, [57, 20])
    coins += 1

    Coin(all_sprites, [57, 520])
    coins += 1

    for i in range(15):
        Coin(all_sprites, [170, 20 * (i * 2 + 1)])
        coins += 1

    for i in range(8):
        Coin(all_sprites, [210 + (20 * i * 2), 20])
        coins += 1

    for i in range(4):
        Coin(all_sprites, [50 + (20 * i * 2), 620])
        coins += 1

    for i in range(18):
        Coin(all_sprites, [250, 60 + (20 * i * 2)])
        coins += 1

    for i in range(6):
        Coin(all_sprites, [20 + (20 * i * 2), 690])
        coins += 1

    for i in range(7):
        Coin(all_sprites, [20 + (20 * i * 2), 760])
        coins += 1

    for i in range(7):
        Coin(all_sprites, [270 + (20 * i * 2), 690])
        coins += 1

    Coin(all_sprites, [20, 727])
    coins += 1

    for i in range(7):
        Coin(all_sprites, [520, 30 + (20 * i * 2)])
        coins += 1

    for i in range(3):
        Coin(all_sprites, [560, 270 + (20 * i * 2)])
        coins += 1

    for i in range(9):
        Coin(all_sprites, [520, 350 + (20 * i * 2)])
        coins += 1

    for i in range(4):
        Coin(all_sprites, [290 + (20 * i * 2), 105])
        coins += 1

    for i in range(13):
        Coin(all_sprites, [330, 145 + (20 * i * 2)])
        coins += 1

    for i in range(4):
        Coin(all_sprites, [370 + (20 * i * 2), 625])
        coins += 1

    for i in range(3):
        Coin(all_sprites, [440, 105 + (20 * i * 2)])
        coins += 1

    for i in range(3):
        Coin(all_sprites, [440, 265 + (20 * i * 2)])
        coins += 1

    for i in range(5):
        Coin(all_sprites, [440, 425 + (20 * i * 2)])
        coins += 1

    for i in range(2):
        Coin(all_sprites, [360 + (20 * i * 2), 185])
        coins += 1

    for i in range(2):
        Coin(all_sprites, [360 + (20 * i * 2), 265])
        coins += 1

    for i in range(2):
        Coin(all_sprites, [360 + (20 * i * 2), 525])
        coins += 1

    for ghost_color_number in range(1, level):
        Ghost(all_sprites, [325, 380], ghost_color_number % 5)

    images = load_images(path='data')

    player = AnimatedSprite(position=(10, 10), images=images)

    all_sprites_pl = pygame.sprite.Group(player)

    screen.fill((100, 100, 100))

    clock = pygame.time.Clock()

    running = True
    while running:
        dt = clock.tick(FPS) / 500
        screen.fill((100, 100, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                if event.key == pygame.K_RIGHT:
                    if player.can_move_x != 1:
                        player.velocity.x = 5
                elif event.key == pygame.K_LEFT:
                    if player.can_move_x != -1:
                        player.velocity.x = -5
                elif event.key == pygame.K_DOWN:
                    if player.can_move_y != 1:
                        player.velocity.y = 5
                elif event.key == pygame.K_UP:
                    if player.can_move_y != -1:
                        player.velocity.y = -5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    player.velocity.x = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    player.velocity.y = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                if event.key == pygame.K_u:
                    level += 1
                    if level != 8:
                        game_menu()
                    else:
                        win_menu()
            if coins == 0:
                level += 1
                if level != 8:
                    game_menu()
                else:
                    win_menu()

        all_sprites.draw(screen)
        all_sprites_pl.draw(screen)
        all_sprites.update()
        all_sprites_pl.update(dt)
        pygame.display.flip()

        clock.tick(FPS)
    pygame.quit()


def lose_menu():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    global can_w

    screen.fill((100, 100, 100))
    draw4(screen)

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
                if event.key == pygame.K_n and can_w == 1:
                    can_w = 0
                    f = open('leaders.txt', 'r')
                    data = list()
                    for i in f.read().split('\n'):
                        if i != '':
                            data.append(i)
                    if data[-1].split(';')[0] != 'player':
                        pl_number = int(data[-1].split(';')[0]) + 1
                    else:
                        pl_number = 1
                    f.close()
                    f = open('leaders.txt', 'w')
                    f.write('\n'.join(data) + '\n')
                    f.write(str(pl_number) + ';' + str(collected_coins))
                    f.close()

        pygame.display.flip()
    pygame.quit()


def win_menu():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    global can_w

    screen.fill((100, 100, 100))
    draw3(screen)

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
                if event.key == pygame.K_n and can_w == 1:
                    can_w = 0
                    f = open('leaders.txt', 'r')
                    data = list()
                    for i in f.read().split('\n'):
                        if i != '':
                            data.append(i)
                    if data[-1].split(';')[0] != 'player':
                        pl_number = int(data[-1].split(';')[0]) + 1
                    else:
                        pl_number = 1
                    f.close()
                    f = open('leaders.txt', 'w')
                    f.write('\n'.join(data) + '\n')
                    f.write(str(pl_number) + ';' + str(collected_coins))
                    f.close()

        pygame.display.flip()
    pygame.quit()


def rules_menu():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)

    screen.fill((100, 100, 100))
    draw2(screen)

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


def leader_menu():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)

    screen.fill((100, 100, 100))
    draw5(screen)

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