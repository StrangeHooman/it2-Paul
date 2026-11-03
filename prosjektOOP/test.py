from blessed import Terminal
from ui import *
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
    

def lerp(val, max, min):
    return (max-min)*val + min

def inverseLerp(val, min, max):
    return (val-min)/(max-min)

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
            currentColor = term.color_rgb(*cell.fg.values) + term.on_color_rgb(*cell.bg.values)
            currentStyles = cell.styles
            
            if lastColor != currentColor:
                outString += currentColor
                lastColor = currentColor

            if lastStyles != currentStyles:

                if currentStyles == ["\x1b[0m"]:
                    outString += currentColor

                else:
                    outString += "\x1b[0m" + currentColor
                    for style in currentStyles: outString += style
                lastStyles = currentStyles


            outString += cell.char

    print(term.move_xy(0, 0) + outString, end="", flush=True)



term = Terminal()

print(term.color_rgb(*defaultColorFront.values) + term.on_color_rgb(*defualtColorBack.values))


screenBuffer = []

screenBuffer = clearBuffer(term)

renderScreen(term, screenBuffer)



startPos = Vector2(*term.get_location())



drawArea = Vector2(0, 0)

newspaperPos = Vector2(40, 0)
newspaperSize = Vector2(40, 30)



print(term.move_xy(drawArea.x, drawArea.y) + term.width*BOX_LIGHT["h"])

firmsArea = Vector2(int(math.floor(term.width * 0.2)), int(math.floor(term.height*0.5)))

firms = 3

tradingScreen = {
    "button1" : Button(Vector2(0, 0) + drawArea, textToCell("Hello\nWorld!", fg=defaultColorFront, bg=defualtColorBack), clickable=True), #Vector2(firmsArea.x, math.floor(firmsArea.y/firms)), clickable=True),
    "button2" : Button(Vector2(0, firmsArea.y//firms * 1) + drawArea, textToCell("A clickable\nbutton")), #Vector2(firmsArea.x, math.floor(firmsArea.y/firms))),
    "button3" : Button(Vector2(0, firmsArea.y//firms * 2) + drawArea, textToCell("A third\nclickable button"), clickable=True), #Vector2(firmsArea.x, math.floor(firmsArea.y/firms)), clickable = True),
    "newspaper" : Button(newspaperPos, textToCell("\033[1mTODAYS NEWS:\033[0m\n\nA woman has fallen down\na stair. Oh no!\n" + "-"*(newspaperSize.x-2) + "\nI shit my pants.\nThis WILL affect the market.", 0, bg = Vector([239, 230, 210]), fg=Vector([28, 26, 23])), colorBack = Vector([239, 230, 210]), colorFront=Vector([28, 26, 23]), clickable=True) #newspaperSize,
}

text1 = Text(Vector2(50, 20), textToCell("Something happening\n\033[1mThis \033[0mis very interresting\n\nBtw, the height of the terminal is \033[31m" + str(term.height) + "\n\033[0mand the width is \033[32m" + str(term.width)))

lastMouse = Vector2(0, 0)

for item in tradingScreen.values():
    screenBuffer = item.render(term, screenBuffer)

framecount = 0

time = Time()


renderScreen(term, screenBuffer)

if not term.does_mouse(report_motion=True):
    print("This terminal doesn't support mouse-motion reporting.")
else:
    with term.cbreak(), term.hidden_cursor(), term.mouse_enabled(report_motion=True):
        while True:


            time.updateTime()
            

            
            event = term.inkey(timeout=1/120)

            screenBuffer = clearBuffer(term)

            if event.lower() == "q":
                break

            if event.name and event.name.startswith("MOUSE_"):
                x, y = event.mouse_xy
                lastMouse = Vector2(x, y)



                #print(term.move_xy(0, drawArea.y + 15) + term.clear_eol + f"{event.name} at x={x}, y={y}", end="", flush=True)


                # button1.pos = lastMouse + drawArea


            for item in tradingScreen.values():
                if type(item) == Button:
                    item.clicked(lastMouse)

            for item in tradingScreen.values():
                screenBuffer = item.render(term, screenBuffer)

            screenBuffer = text1.render(term, screenBuffer)

            renderScreen(term, screenBuffer)

            framecount += 1


print(term.move_xy(0, drawArea.y+8) + "Hello")
for i in range(term.height):
    print(term.move_xy(0, drawArea.y + i + 1) + " "*term.width, end="", flush=True)

print(term.move_xy(startPos.x, startPos.y))