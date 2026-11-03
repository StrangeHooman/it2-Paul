class Company:
    name: str
    function = None
    functionParams: tuple
    stock = 0
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def getVal(self):
        self.function(*self.functionParams) * self.stock
    

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


def basicStock(seed, )

companies = {
    Company("Biltema", basicStock),
    Company("Jasper CO")
}


articles = {Newspaper("""
""", "")}