import random


class Company:
    name: str
    biasFunciton = None
    biasFunctionParams: tuple
    dailyFunction = None
    dailyFunctionParams: tuple
    shares = 0
    def __init__(self, name, bias, daily):
        self.name = name
        self.biasFunction = bias
        self.dailyFunction = daily

    def getCash(self):
        return self.dailyFunction(self.biasFunciton, *self.functionParams) * self.shares
    

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


def dailyBasicStock(seed, randomIntensity):
    return seed + random.randint() randomIntensity

companies = {
    Company("Biltema", basicStock),
    Company("Jasper CO", )
}


articles = {Newspaper("""
""", "")}