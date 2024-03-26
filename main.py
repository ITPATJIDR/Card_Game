import pygame
import os
import sys
from desk import Desk
from bot import Bot
from player import Player

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
        elif self.state == 2:
            self.result()


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
        self.desired_width = 100
        self.desired_height = 150  
        self.backCard_image = pygame.transform.scale(
            self.backCard_image, (self.desired_width, self.desired_height)
        )
        self.backCard_image_size = self.backCard_image.get_size()

        self.main_card_loc = (625,250) 
        self.bot_1_card_loc = [(150,250),(200,250),(250,250)]
        self.bot_2_card_loc = [(1000,250),(1050,250),(1100,250)]
        self.bot_3_card_loc = [(600,20),(650,20),(700,20)]
        self.player_card_loc = [(600,450),(650,450),(700,450)]

        self.font = pygame.font.Font('font/CoffeeTin.ttf', 50)
        self.finishButton = self.font.render(" Finish ", 1, BLACK)
        self.buttonSize =self.font.size(" Finish ")
        self.buttonLoc = (1000,450)

        self.main_card_Rect = pygame.Rect(self.main_card_loc, self.backCard_image_size)
        self.buttonRect = pygame.Rect(self.buttonLoc, self.buttonSize)
        self.buttonRectOutline = pygame.Rect(self.buttonLoc, self.buttonSize)



    def play(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();sys.exit() 

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouseRect = pygame.Rect(event.pos, (1,1))

                    if mouseRect.colliderect(self.main_card_Rect):
                        if len(player.getCard()) <= 2 :
                            player.addCard(desk.getTopOfDesk())
                            bot_1.draw(desk)
                            bot_2.draw(desk)
                            bot_3.draw(desk)
                        return

                    if mouseRect.colliderect(self.buttonRect):
                        bot_1.draw(desk)
                        bot_2.draw(desk)
                        bot_3.draw(desk)
                        self.state += 1
                        return
        
        if len(bot_1.getCard()) < 2:
            bot_1.addCard(desk.getTopOfDesk())

        if len(bot_2.getCard()) < 2:
            bot_2.addCard(desk.getTopOfDesk())

        if len(bot_3.getCard()) < 2:
            bot_3.addCard(desk.getTopOfDesk())

        if len(player.getCard()) < 2:
            player.addCard(desk.getTopOfDesk())

        #print(f"bot 1 card is  {bot_1.getCard()} and cal is {bot_1.cal()}")
        #print(f"bot 2 card is  {bot_2.getCard()} and cal is {bot_2.cal()}")
        #print(f"bot 3 card is  {bot_3.getCard()} and cal is {bot_3.cal()}")
        #print(f"bot 3 card is  {player.getCard()} and cal is {player.cal()}")

        SCREEN.blit(self.backCard_image, self.main_card_loc)

        for i in range(len(bot_1.getCard())):
            SCREEN.blit(self.backCard_image, self.bot_1_card_loc[i])

        for i in range(len(bot_2.getCard())):
            SCREEN.blit(self.backCard_image, self.bot_2_card_loc[i])

        for i in range(len(bot_3.getCard())):
            SCREEN.blit(self.backCard_image, self.bot_3_card_loc[i])

        for i in range(len(player.getCard())):
            card_images = player.getCard_image() 
            SCREEN.blit(card_images[i], self.player_card_loc[i])

        pygame.draw.rect(SCREEN, RED, self.buttonRect)
        pygame.draw.rect(SCREEN, BLACK, self.buttonRectOutline, 2)
        SCREEN.blit(self.finishButton, self.buttonLoc)

        pygame.display.flip()


    def result(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();sys.exit() 

        for i in range(len(bot_1.getCard())):
            card_images = bot_1.getCard_image() 
            SCREEN.blit(card_images[i], self.bot_1_card_loc[i])

        for i in range(len(bot_2.getCard())):
            card_images = bot_2.getCard_image() 
            SCREEN.blit(card_images[i], self.bot_2_card_loc[i])

        for i in range(len(bot_3.getCard())):
            card_images = bot_3.getCard_image() 
            SCREEN.blit(card_images[i], self.bot_3_card_loc[i])

        for i in range(len(player.getCard())):
            card_images = player.getCard_image() 
            SCREEN.blit(card_images[i], self.player_card_loc[i])
        
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
    bot_2 = Bot()
    bot_3 = Bot()
    player = Player()
    Myclock = pygame.time.Clock()

    while True:
        SCREEN.blit(background_image, (0, 0))
        board.main()
        Myclock.tick(64)
