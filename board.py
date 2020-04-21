import pygame


class BoardRenderer:
    def __init__(self,screen):
        x = 0
        y = 0
        for i in range(8):
            for j in range(8):
                if i % 2 == 0 and j % 2 == 0:
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, 99, 74))
                if i % 2 == 1 and j % 2 == 1: 
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, 99, 74))
                if i % 2 == 0 and j % 2 == 1: 
                    pygame.draw.rect(screen, (101, 67, 33), (x, y, 99, 74))
                if i % 2 == 1 and j % 2 == 0: 
                    pygame.draw.rect(screen, (101, 67, 33), (x, y, 99, 74))
                x += 100
            
            y += 75
            x = 0
