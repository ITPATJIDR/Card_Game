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
                calArray.append(int(value))
            result = sum(calArray) 
            convertResult = str(result)

            if result >= 10:
                print(convertResult[1])
            else: 
                print(convertResult[0])
