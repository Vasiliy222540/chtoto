import pygame

FPS = 30
pygame.init()
pygame.mixer.init()
WIDTH = 360
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My game')
running = True
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
screen.fill(RED)
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()






