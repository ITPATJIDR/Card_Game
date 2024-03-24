class Bot :
        def __init__(self):
            self.cards = []

        def addCard(self,newCard):
            self.cards.append(newCard)

        def getCard(self):
            return self.cards 
