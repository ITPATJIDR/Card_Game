import pygame
import os
import sys
from desk import Desk
from bot import Bot

BLACK = (255,255,255)
BLACK = (0,0,0)
GREY  = (50,50,50)
RED  = (207,0,0)


WIDTH = 1280
HEIGHT = 720

class Board: 
    def __init__(self):
        self.state = 0
        self.start_up_init()
        self.backCard_path = os.path.join(current_dir, 'img', 'back.png')
        self.backCard_image = pygame.image.load(self.backCard_path).convert_alpha()

    def main(self):
        if self.state == 0:
            self.start()
        elif self.state == 1:
            self.play()


    def start_up_init(self):
        self.font = pygame.font.Font('font/CoffeeTin.ttf', 50)
        self.startButton = self.font.render(" Start ", 1, BLACK)
        self.buttonSize =self.font.size(" Start ")
        self.buttonLoc = (WIDTH/2 - self.buttonSize[0]/2, HEIGHT/2 - self.buttonSize[1]/2)

        self.buttonRect = pygame.Rect(self.buttonLoc, self.buttonSize)
        self.buttonRectOutline = pygame.Rect(self.buttonLoc, self.buttonSize)


    def start(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();sys.exit() 

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouseRect = pygame.Rect(event.pos, (1,1))
                    if mouseRect.colliderect(self.buttonRect):
                        self.state += 1
                        desk.shuffle()
                        self.play_init()
                        return


        pygame.draw.rect(SCREEN, RED, self.buttonRect)
        pygame.draw.rect(SCREEN, BLACK, self.buttonRectOutline, 2)
        SCREEN.blit(self.startButton, self.buttonLoc)
        pygame.display.flip()


    def play_init(self):
        self.desired_width = 50  
        self.desired_height = 100  
        self.backCard_image = pygame.transform.scale(
            self.backCard_image, (self.desired_width, self.desired_height)
        )
        self.backCard_image_size = self.backCard_image.get_size()

        self.backCard_image_desk_loc = (WIDTH/2 - self.backCard_image_size[0]/2, HEIGHT/2 - self.backCard_image_size[1]/2)
        self.backCard_image_bot_1 = (WIDTH/6 - self.backCard_image_size[0]/2, HEIGHT/2 - self.backCard_image_size[1]/2)
        self.backCard_image_bot_2 = (WIDTH/2 - self.backCard_image_size[0]/2, HEIGHT/6 - self.backCard_image_size[1]/2)
        self.backCard_image_bot_3 = (1010, HEIGHT/2 - self.backCard_image_size[1]/2)

    def play(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();sys.exit() 
        
        if len(bot_1.getCard()) != 2:
            bot_1.addCard(desk.getTopOfDesk())

        print(bot_1.cal())
        #SCREEN.blit(self.backCard_image, self.backCard_image_desk_loc)
        #SCREEN.blit(self.backCard_image, self.backCard_image_bot_1)
        #SCREEN.blit(self.backCard_image, self.backCard_image_bot_2)
        #SCREEN.blit(self.backCard_image, self.backCard_image_bot_3)

        pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("ป็อก 9 สอง เด้ง")
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT),0, 32)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    background_image_path = os.path.join(current_dir, 'img', 'background.jpg')
    background_image = pygame.image.load(background_image_path)

    board = Board()
    desk = Desk(current_dir)
    bot_1 = Bot()
    Myclock = pygame.time.Clock()

    while True:
        SCREEN.blit(background_image, (0, 0))
        board.main()
        Myclock.tick(64)
