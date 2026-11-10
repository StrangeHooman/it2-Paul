from tools      import *
import random


class Company:
    name: str
    model: function
    quarterlyParams: tuple
    dailyParams: tuple
    nodeParams: tuple
    shares = 0
    def __init__(self, name, model, quarterlyParams, dailyParams, nodeParams):
        self.name = name
        self.model = model
        self.quarterlyParams = quarterlyParams
        self.dailyParams = dailyParams
        self.nodeParams = nodeParams

    def getNodes(self):
        quarterly = self.model(*self.quarterlyParams)

        final = []

        for i, day in enumerate(quarterly):
            daily = self.model(*self.dailyParams)
            nodes = self.model(*self.nodeParams)

            currentDay = []

            nodeCount = 0
            lastPos = 0

            for j, val in enumerate(daily):



                if j == len(daily) - 1:
                    randomAddition = len(nodes)

                else:
                    randomAddition = round((j+1) * (len(nodes[:-1])/len(daily[:-1]))) + random.randint(0, 0)                


                for k in range(lastPos, randomAddition):
                    try:
                        currentDay.append(lerp(invLerp(k, lastPos, randomAddition), daily[j], daily[j+1]) + nodes[nodeCount] + day)

                    except:
                        currentDay.append(daily[j] + nodes[nodeCount] + day)

                    nodeCount += 1


                lastPos = randomAddition

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


def noiseCalc(amplitude, amount, bias = 0):
    return [(round(amplitude*bias) + random.randint(-amplitude, amplitude)) for i in range(amount)]

# Distance is needed change to get to target. Value 2 target 1 has a distance of -2 because you must divide by 2.
def noiseCalc(amplitude, amount, distance, centering = 1, bias = 0):
    return [round(lerp(centering, percentage(sign(random.uniform(-1, 1) + bias) * random.uniform(1, amplitude)), distance)) for i in range(amount)]

companies = {
    "Biltema": Company("Biltema", noiseCalc, (0, 1), (8, 5, 1), (3, 46*3, 1)),
    "Jasper CO" : Company("Jasper CO", noiseCalc, (0, 1), (0, 1), (2, 3))
}


articles = {Newspaper("""
""", "", 0)}