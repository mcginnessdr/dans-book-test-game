import pygame, os, time, random



class Game():
    def __init__(self):
        pygame.init()
        self.WIN_WIDTH, self.WIN_HEIGHT = 1000, 800
        self.WIN = pygame.display.set_mode((self.WIN_WIDTH, self.WIN_HEIGHT))
        self.WIN_TITLE = pygame.display.set_caption("Dan's Book - Test Game")
        self.FONT = pygame.font.SysFont("impact", 20)
        self.BG = pygame.image.load("backgroundimage.jpeg")
        self.CANVAS = pygame.Surface((self.WIN_WIDTH, self.WIN_HEIGHT)) # NEED TO STUDY
        self.running, self.playing = True, True # NEED TO STUDY
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
        self.dt, self.prev_time = 0, 0 # NEED TO STUDY
        self.state_stack = [] # NEED TO STUDY
        self.load_assets() 



    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    self.playing = False
                    self.running = False
                if event.key == pygame.K_a:
                    self.actions["left"] = True
                if event.key == pygame.K_d:
                    self.actions["right"] = True
                if event.key == pygame.K_w:
                    self.actions["up"] = True
                if event.key == pygame.K_s:
                    self.actions["down"] = True
                if event.key == pygame.K_q:
                    self.actions["action_1"] = True
                if event.key == pygame.K_e:
                    self.actions["action_2"] = True
                if event.key == pygame.K_BACKSPACE:
                    self.actions["back"] = True
                if event.key == pygame.K_RETURN:
                    self.actions["enter"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.actions["left"] = False
                if event.key == pygame.K_d:
                    self.actions["right"] = False
                if event.key == pygame.K_w:
                    self.actions["up"] = False
                if event.key == pygame.K_s:
                    self.actions["down"] = False
                if event.key == pygame.K_q:
                    self.actions["action_1"] = False
                if event.key == pygame.K_e:
                    self.actions["action_2"] = False
                if event.key == pygame.K_BACKSPACE:
                    self.actions["back"] = False
                if event.key == pygame.K_RETURN:
                    self.actions["enter"] = False



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
        