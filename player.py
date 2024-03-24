class player :
        def __init__(self):
            self.Cards = []
        
        def addCard(self,newCard):
            self.Cards.append(newCard)

        def getCard(self):
            return self.Cards
