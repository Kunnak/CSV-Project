import pygame
import random

pygame.init()

SCREEN = WIDTH, HEIGHT = 288 * 2, 512 * 2

info = pygame.display.Info()
width = 500
height = 900

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)

punkte = 0
speed = 3

class Rectangle:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.width = 99
        self.height = 175
        self.speed = speed

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height))

    def move(self):
        self.y += self.speed

    def is_clicked(self, pos):
        return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height

def spawn_rectangle():
    random_int = random.randint(1, 6)
    return (random_int * 100) - 100

rectangles = []

for i in range(5):
    rectangles.append(Rectangle(spawn_rectangle(), -200, speed))

running = True

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
                    if rectangle.is_clicked(event.pos) and rectangle.y > 20:
                        rectangles.remove(rectangle)
                        speed = speed + 0.05
                        rectangle.speed = speed

    for rectangle in rectangles[:]:
        rectangle.move()
        rectangle.draw(screen)
        if rectangle.y >= height:
            rectangles.remove(rectangle)
            rectangles.append(Rectangle(spawn_rectangle(), -200, speed))

    if rectangle.y >= -25:
        rectangles.append(Rectangle(spawn_rectangle(), -200, speed))

    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
