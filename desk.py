import os
import random

class Desk :
        def __init__(self, current_dir):
            self.Desk = []
            self.deskPath = os.path.join(current_dir, 'img')
            self.getCard()

        def getCard(self):
            files = os.listdir(self.deskPath)[:-2]
            for i in range(len(files)):
                splitName = files[i].split(".")[0]
                self.Desk.append(splitName)

        def shuffle(self):
            random.shuffle(self.Desk)

        def getTopOfDesk(self):
            topDesk = self.Desk[0] 
            self.Desk.pop(0) 
            return topDesk

