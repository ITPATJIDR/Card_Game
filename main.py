import pygame
import os
import sys

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

    def main(self):
        if self.state == 0:
            self.start()


    def start_up_init(self):
        font = pygame.font.Font('font/CoffeeTin.ttf', 50)
        self.loadText = font.render("Loading...", 1, BLACK)
        self.loadSize = font.size("Loading...")
        self.loadLoc = (WIDTH/2 - self.loadSize[0]/2, HEIGHT/2 - self.loadSize[1]/2)


    def start(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();sys.exit() 

        SCREEN.blit(self.loadText, self.loadLoc)
        pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("ป็อก 9 สอง เด้ง")
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT),0, 32)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    background_image_path = os.path.join(current_dir, 'img', 'background.jpg')
    background_image = pygame.image.load(background_image_path)

    board = Board()
    Myclock = pygame.time.Clock()

    while True:
        SCREEN.blit(background_image, (0, 0))
        board.main()
        Myclock.tick(64)
