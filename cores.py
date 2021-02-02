import pygame
import random

pygame.init()



windonw = pygame.display.set_mode((500, 500))

loop = True

clock = pygame.time.Clock()
     

while loop:
        clock.tick(6)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        loop = False
        R = random.randint(0, 225)
        G = random.randint(0, 225)
        B = random.randint(0, 225)

        windonw.fill((R, G, B,))



        
        
        pygame.display.update()

        