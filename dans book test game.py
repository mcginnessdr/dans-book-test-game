import pygame
import time
import random


WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dan's Book - Test Game") # title of game window
pygame.font.init()
FONT = pygame.font.SysFont("impact", 25) # change game font and font size
BG = pygame.image.load("backgroundimage.jpeg") # change background image


class Library():
    def __init__(self):
        def ...

class Book():
    def __init__(self):
        self.title = ""
        self.sub_title = ""
        self.author = ""

class Page():
    def __init__(self):
        self.page_num = 0
        self.page_title = ""
        self.page_sub_title = ""
        self.body_text = ""

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

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    

def draw():
    WIN.blit(BG, (0, 0))

    pygame.display.update()


def main_menu():


def library():
    
    def create_new_book():

    def edit_book():

    def delete_book():

    
    
def exit()
    


if __name__ == "__main__":
    main()