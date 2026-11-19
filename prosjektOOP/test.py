from blessed import Terminal
from ui         import *
from gameData   import *
from tools      import *
import time as timeLib
import math
import re

class Time:
    timeScale = 1.0
    gameTime = 0.0
    realTime = 0.0
    deltaTime = 0
    unscaledDeltaTime = 0

    def __init__(self):
        self.lastTime = timeLib.perf_counter()
        self.startTime = self.lastTime

    def updateTime(self):
        lastTime = self.lastTime
        currentTime = timeLib.perf_counter()

        self.unscaledDeltaTime = currentTime - lastTime
        self.deltaTime = self.unscaledDeltaTime * self.timeScale
        self.gameTime += self.deltaTime
        self.realTime += self.unscaledDeltaTime
        self.lastTime = currentTime
    



def clearBuffer(term: Terminal):
    global defaultCell

    buffer = []
    for i in range(term.height):
        buffer.append([defaultCell for i in range(term.width)])

    return buffer

def renderScreen(term: Terminal, buffer):

    lastColor = None
    lastStyles = None
    outString = ""

    for row, string in enumerate(buffer):
        for col, cell in enumerate(string):
            currentColor = term.color_rgb(*[clamp(round(val), 0, 255) for val in cell.fg.values]) + term.on_color_rgb(*[clamp(round(val), 0, 255) for val in cell.bg.values])
            currentStyles = cell.styles
            
            if lastColor != currentColor:
                outString += currentColor
                lastColor = currentColor

            if lastStyles != currentStyles:

                if currentStyles == ["\x1b[0m"]:
                    outString += "\x1b[0m" + currentColor

                else:
                    outString += "\x1b[0m" + currentColor
                    for style in currentStyles: outString += style
                lastStyles = currentStyles


            outString += cell.char

    print(term.move_xy(0, 0) + outString, end="", flush=True)


def calcStocks(startPos, endPos, nodesPerStock, currentNode):

    
    companyStocks = []

    for company in companies.values():
        nodes = company.nodes
        stocks = []


        currentNode = min(currentNode, len(nodes[0])-8)

        space = clamp(math.floor((endPos.x - startPos.x)/2) + 1, 0, math.ceil((len(nodes[0][0:currentNode])-1)/nodesPerStock)) 


        realStart = endPos.x - math.floor((len(nodes[0][0:currentNode])-1)/nodesPerStock * 2)


        for i in range(0, currentNode, 9):
            stocks.append(chartBar(Vector2(realStart + 2*i//9, 40), Vector(nodes[0][i:i+10])))

        companyStocks.append(stocks[-space:])

    return companyStocks


term = Terminal()

print(term.color_rgb(*defaultColorFront.values) + term.on_color_rgb(*defaultColorBack.values))


screenBuffer = []

screenBuffer = clearBuffer(term)

renderScreen(term, screenBuffer)



startPos = Vector2(*term.get_location())



drawArea = Vector2(0, 0)

newspaperPos = Vector2(40, 0)
newspaperSize = Vector2(40, 30)



print(term.move_xy(drawArea.x, drawArea.y) + term.width*BOX_LIGHT["h"])






#text5 = Text(Vector2(0, 0), textToCell("nodesList is " + str([round(num) for num in nodes[0]])))

companyStocks = calcStocks(Vector2(22, 0), Vector2(100, 25), 9, 45*9+1)

green = defaultGreen
red = defaultRed
text = Vector([0, 0, 0])

utilButtons = {
    "BUY" : Button(Vector2(19, 26), textToCell(" \033[1mBUY\033[0m ", bg=green, fg=text), colorBack=green, colorFront=text, clickable=True),
    "SELL" : Button(Vector2(30, 26), textToCell(" \033[1mSELL\033[0m ", bg=red, fg=text), colorBack=red, colorFront=text, clickable=True),
}

ui = [
    Text(Vector2(19, 30 - 30), textToCell("\n".join([str(i+15) for i in range(25, 0, -1)]), 2)),
    Text(Vector2(19, 25), textToCell(BOX_OUTER["t"]*(term.width - 19)))
]

firmsArea = Vector2(int(math.floor(term.width * 0.2)), int(math.floor(term.height*0.5)))

firms = len(companies)

tradingScreen = {
    "button1" : Button(Vector2(0, 0) + drawArea, textToCell(list(companies.values())[0].name, 1), clickable=True, function = returnNum, funcArgs = (0,)), #Vector2(firmsArea.x, math.floor(firmsArea.y/firms)), clickable=True),
    "button2" : Button(Vector2(0, firmsArea.y//firms * 1) + drawArea, textToCell(list(companies.values())[1].name, 1), clickable=True, function = returnNum, funcArgs = (1,)), #Vector2(firmsArea.x, math.floor(firmsArea.y/firms))),
    "button3" : Button(Vector2(0, firmsArea.y//firms * 2) + drawArea, textToCell(list(companies.values())[2].name, 1), clickable=True, function = returnNum, funcArgs = (2,)), #Vector2(firmsArea.x, math.floor(firmsArea.y/firms)), clickable = True),
    #"newspaper" : Button(newspaperPos, textToCell("\033[1mTODAYS NEWS:\033[0m\n\nA woman has fallen down\na stair. Oh no!\n" + "-"*(newspaperSize.x-2) + "\nI shit my pants.\nThis WILL affect the market.", 0, bg = Vector([239, 230, 210]), fg=Vector([28, 26, 23])), colorBack = Vector([239, 230, 210]), colorFront=Vector([28, 26, 23]), clickable=True) #newspaperSize,
}

lastMouse = Vector2(0, 0)

for item in tradingScreen.values():
    screenBuffer = item.render(term, screenBuffer)

framecount = 0

time = Time()

selectedCompany = 0
cash = 0

testText = Text(Vector2(0, 0), textToCell(" "))

renderScreen(term, screenBuffer)

if not term.does_mouse(report_motion=True):
    print("This terminal doesn't support mouse-motion reporting.")
else:
    with term.cbreak(), term.hidden_cursor(), term.mouse_enabled(report_motion=True):
        while True:

            time.updateTime()

            clicking = False
            
            event = term.inkey(timeout=1/120)

            screenBuffer = clearBuffer(term)

            companyStocks = calcStocks(Vector2(22, 0), Vector2(110, 25), 9, round(cash*200))   

            if event.lower() == "q":
                break



            if event.name and event.name.startswith("MOUSE_"):
                x, y = event.mouse_xy
                lastMouse = Vector2(x, y)


                if event.name == "MOUSE_LEFT":
                    clicking = True

                testText = Text(Vector2(0, 0), textToCell(event.name))

                #print(term.move_xy(0, drawArea.y + 15) + term.clear_eol + f"{event.name} at x={x}, y={y}", end="", flush=True)


                # button1.pos = lastMouse + drawArea


            for item in tradingScreen.values():
                if type(item) == Button:
                    selectedCompany = item.clicked(lastMouse, clicking) if item.clicked(lastMouse, clicking) != None else selectedCompany

            for item in utilButtons.values():
                if type(item) == Button:
                    item.clicked(lastMouse, False)


            for item in tradingScreen.values():
                screenBuffer = item.render(term, screenBuffer)

            for item in utilButtons.values():
                screenBuffer = item.render(term, screenBuffer)


            #text1 = Text(Vector2(50, 20), textToCell("Something happening\n\033[1mThis \033[0mis very interresting\n\nBtw, the height of the terminal is \033[31m" + str(term.height) + "\n\033[0mand the width is \033[32m" + str(term.width)))

            cashText = Text(Vector2(45, 27), textToCell(str(round(cash)) + "$"))

            screenBuffer = cashText.render(term, screenBuffer)

            for stock in companyStocks[selectedCompany]:
                screenBuffer = stock.render(term, screenBuffer)

            #screenBuffer = testText.render(term, screenBuffer)

            for item in ui:
                screenBuffer = item.render(term, screenBuffer)

            renderScreen(term, screenBuffer)

            framecount += 1
            cash += 1 * time.deltaTime


print(term.move_xy(0, drawArea.y+8) + "Hello")
for i in range(term.height):
    print(term.move_xy(0, drawArea.y + i + 1) + " "*term.width, end="", flush=True)

print(term.move_xy(startPos.x, startPos.y))