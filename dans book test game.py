import pygame
import time
import random


WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dan's Book - Test Game") # title of game window
pygame.font.init()
FONT = pygame.font.SysFont("impact", 50) # change game font and font size
BG = pygame.image.load("backgroundimage.jpeg") # change background image


class Book():
    def __init__(self):
        self.title = ""
        self.sub_title = ""
        self.author = ""
        self.open_or_close = 0

class Page():
    def __init__(self):
        self.page_num = 0
        self.page_title = ""
        self.page_sub_title = ""
        self.body_text = ""
        self.left_or_right = 0

class Author():
    def __init__(self):
        self.f_name = ""
        self.l_name = ""
        self.password = ""


def main():
    run = True
    
    while run:

         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break



if __name__ == "__main__":
    main()