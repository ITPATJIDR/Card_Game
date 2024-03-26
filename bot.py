import os
import pygame

class Bot :
        def __init__(self):
            self.cards = []

        def addCard(self,newCard):
            self.cards.append(newCard)

        def getCard(self):
            return self.cards 

        def cal(self):
            calArray = []

            for card in self.cards:
                value = ''.join(filter(str.isdigit, card))
                calArray.append(self.checkHighCard(value))

            result = sum(calArray) 
            convertResult = str(result)

            if result >= 10:
                return convertResult[1]
            else: 
                return convertResult[0]

        def getCard_image(self):
            card_images = []
            current_dir = os.path.dirname(os.path.abspath(__file__))
            for i in self.cards:
                newImagePath = i + ".png"
                image_path = os.path.join(current_dir, 'img', str(newImagePath))
                card_image = pygame.image.load(image_path)
                card_images.append(card_image)

            return card_images

        def draw(self, desk):
            topDeskValue = int(''.join(filter(str.isdigit, desk.getDesk()[0])))
            calResult = self.cal()

            if (int(calResult) + topDeskValue) > int(calResult) and (int(calResult) + topDeskValue) <= 9:
                self.cards.append(desk.getTopOfDesk())
            else:
                print("not Draw")


        def checkHighCard(self,value):
            if int(value) >= 10 and int(value) <= 13:
                return 0 
            elif int(value) == 14:
                return 1
            else:
                return int(value)


            


            
