import pygame, os, time, random




class Game():
    def __init__(self):
        pygame.init()
        self.WIN_WIDTH, self.WIN_HEIGHT = 1000, 800
        self.WIN = pygame.display.set_mode((self.WIN_WIDTH, self.WIN_HEIGHT))
        self.WIN_TITLE = pygame.display.set_caption("Dan's Book - Test Game")
        self.FONT = pygame.font.SysFont("impact", 20)
        self.BG = pygame.image.load("backgroundimage.jpeg")
        self.CANVAS = pygame.Surface((self.WIN_WIDTH, self.WIN_HEIGHT))
        #self.running, self.playing = True, True
        self.actions = {
            "left" : False,
            "right" : False,
            "up" : False,
            "down" : False,
            "action_1" : False,
            "action_2" : False,
            "back" : False,
            "enter" : False
        }
        #self.dt, self.prev_time = 0, 0
        #self.state_stack = []
        #self.load_assets()



class Library():
    def __init__(self):
        self.book_shelf = {
            "slot_1" : False,
            "slot_2" : False,
            "slot_3" : False
        }




class Book():
    def __init__(self):
        self.book_title = ""
        self.book_sub_title = ""
        self.book_author = ""




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
