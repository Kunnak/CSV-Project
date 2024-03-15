import time

import pygame
import random

pygame.init()

info = pygame.display.Info()
width = 500
height = 900

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)

leben = 30
punkte = 0
speed = 3
i = 1
spawn_bool = True


class Rectangle:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.width = 99
        self.height = 190
        self.speed = speed

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height), 10)

    def move(self):
        self.y += self.speed

    def is_clicked(self, pos):
        return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height


def spawn_rectangle():
    random_int = random.randint(1, 6)
    return (random_int * 100) - 100


rectangles = []

for i in range(4):
    rectangles.append(Rectangle(spawn_rectangle(), -400, speed))

running = True


def game_loop():
    global running, speed, punkte, leben, i, spawn_bool
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    for rectangle in rectangles[:]:
                        if rectangle.is_clicked(event.pos):
                            rectangles.remove(rectangle)

                            speed = speed + 0.05
                            rectangle.speed = speed
                            punkte = punkte + 1

        pygame.draw.line(screen, (0, 0, 0), (0, 700), (500, 700), 10)
        pygame.draw.rect(screen, RED, (0, 702, 500, 900))

        for rectangle in rectangles[:]:
            rectangle.move()
            rectangle.draw(screen)

            if rectangle.y > height:
                rectangles.remove(rectangle)

        if rectangle.y >= -200:
            rectangles.append(Rectangle(spawn_rectangle(), -400, speed))



        clock.tick(FPS)
        pygame.display.update()

        if leben <= 10:
            running = False

    pygame.quit()
