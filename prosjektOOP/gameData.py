from tools      import *
import random


class Company:
    name: str
    model: function
    quarterlyParams: tuple
    dailyParams: tuple
    nodeParams: tuple
    nodes = []
    shares = 0

    def __init__(self, name, model, offset, randomDiff, quarterlyParams, dailyParams, nodeParams):
        self.name = name
        self.model = model
        self.offset = offset
        self.quarterlyParams = quarterlyParams
        self.dailyParams = dailyParams
        self.nodeParams = nodeParams
        self.randomDiff = randomDiff
        self.nodes = self.getNodes()

    def changeShare(self, price, money, amnt):
        if amnt > 0:
            if money >= (price * amnt + 2):
                self.shares += amnt
                money -= price * amnt + 2

        else:
            if -amnt <= self.shares:
                self.shares += amnt
                money -= price * amnt

        return money


    def getNodes(self):                                             # Må bruke forskjellige modeller for daglig og quarterly, og node. Bruk distToPercent funksjonen.
        lastNode = self.offset
        
        quarterly = [self.model(lastNode, self.offset, *self.quarterlyParams[1:]) for i in range(self.quarterlyParams[0])]

        lastNode = quarterly[-1]

        print(type(quarterly[0]))

        final = []

        for i, day in enumerate(quarterly):
            daily = []
            lastDay = lastNode
            for i in range(self.dailyParams[0]):
                daily.append(self.model(lastDay, day, *self.dailyParams[1:]))
                lastDay = daily[-1]

            print(daily)

            #nodes = [self.model(0, *self.nodeParams[1:]) for i in range(self.nodeParams[-1])]

            currentDay = []

            nodeCount = 0
            lastPos = 0
            
            for j, val in enumerate(daily):

                randomAddition = 0

                if j == len(daily) - 1:
                    randomAddition = self.nodeParams[0] + 1

                elif j == len(daily) - 2:
                    randomAddition = self.nodeParams[0]

                else:
                    randomAddition = round((j+1) * ((self.nodeParams[0])/(self.dailyParams[0]-1))) + random.randint(-self.randomDiff, self.randomDiff)                


                for k in range(lastPos, randomAddition):
                    try:
                        target = lerp(invLerp(k, lastPos, randomAddition), daily[j], daily[j+1])


                    except:
                        target = daily[j]

                    amount = self.model(lastNode, target, *self.nodeParams[1:])

                    currentDay.append(amount)

                    nodeCount += 1

                    lastNode = currentDay[-1]

                    print(k)


                lastPos = randomAddition


            print(nodeCount)
            final.append(currentDay)


        
        return final
    

class TextBlocks:
    text: str

    def __init__(self, text):
        self.text = text

class Newspaper(TextBlocks):
    firm: str
    baseEffect: float
    def __init__(self, text, firm, baseEffect):
        super().__init__(text)
        self.firm = firm
        self.baseEffect = baseEffect


def noiseCalc(current: float, target: float, min, max, minAmp, maxAmp, bias = 0, centering = 0, edgeCentering = 0):
    k = 0.35
    
    tryNode = sign(random.uniform(-1, 1) + bias) * random.uniform(minAmp, maxAmp) + current
    
    centeringOffset = (target - tryNode) * centering

    midpoint = (min + max)/2


    value = tryNode + centeringOffset

    minWidth = lerp(edgeCentering, min, midpoint)
    maxWidth = lerp(edgeCentering, max, midpoint)

    minCloseness = invLerp(value, minWidth, min)
    maxCloseness = invLerp(value, maxWidth, max)

    minCloseness = clamp(0 if minCloseness < 0 else minCloseness, 0, 1)
    maxCloseness = clamp(0 if maxCloseness < 0 else maxCloseness, 0, 1)


    minMaxCentering = k * (minWidth - min) * minCloseness**2 - k * (max - maxWidth) * maxCloseness**2

    return clamp(value + minMaxCentering, min, max)

# Distance is needed change to get to target. Value 2 target 1 has a distance of -2 because you must divide by 2.
#def noiseCalc(min, position, max, amplitude, amount, centering = 0, bias = 0):
    # return [lerp(centering, sign(random.uniform(-1, 1) + bias) * random.uniform(1, amplitude), distance) for i in range(amount)]

    # finalNodes = []
    # for i in range(amount):
    #     if 

companies = {
    "Biltema": Company(" Biltema ", noiseCalc, 15, 10, (1, 16, 40, 0, 10, 0, 0.1, 0.1), (6, 21, 35, 0, 10, 0, 0.25, 0.5), (45*3*3+1, 16, 40, 0, 3, 0, 0.4, 0.1)),           # Gjør det mulig å bestemme egen modell for hver noise
    "Jasper CO" : Company(" Jasper \n & CO ", noiseCalc, 15, 10, (1, 16, 40, 5, 15, 0, 0.1, 0.25), (6, 18, 38, 5, 20, 0, 0.25, 0.5), (45*3*3+1, 16, 40, 1, 5, 0, 0.4, 0.25)),
    "Lethal company" : Company(" Lethal \n company ", noiseCalc, 0, 6, (1, 16, 40, 0, 5, 1, 0.1, 0.1), (9, 16, 40, 10, 20, -0.65, 0, 0.1), (45*3*3+1, 16, 40, 0, 5, 0, 0.5, 0.25))
}


articles = {Newspaper("""
""", "", 0)}