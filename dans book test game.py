import pygame
import time
import random


WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dan's Book - Test Game") # title of game window
pygame.font.init()
FONT = pygame.font.SysFont("impact", 30) # change game font and font size
BG = pygame.image.load("backgroundimage.jpeg") # change background image


class Library():
    def __init__(self):
        self.

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

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    

def draw():
    WIN.blit(BG, (0, 0))

    pygame.display.update()


def main_menu():

    def exit_game():

    def library():


        def book():

        def save_progress():

        def delete_book():

        def publish_book():


def author():

    def new_author():

    def edit_author(:)

    def delete_author():


def left_page():

    def new_page():

    def edit_page():

    def delete_page():


def right_page():

    def new_page():

    def edit_page():

    def delete_page():


def title():

    def edit_title():


def body():

    def edit_body():


def page_num():

    def add_page_num():
    
    def delete_page_num():


if __name__ == "__main__":
    main()