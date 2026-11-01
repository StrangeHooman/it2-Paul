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
    outString = ""

    for row, string in enumerate(buffer):
        for col, cell in enumerate(string):
            currentColor = term.color_rgb(*cell.fg) + term.on_color_rgb(*cell.bg)
            
            if lastColor != currentColor:
                outString += currentColor
                lastColor = currentColor

            outString += cell.char

    print(term.move_xy(0, 0) + outString, end="", flush=True)

def textToCell(string: str, horizontalLayout = 0, *, fg = (212, 212, 212), bg = (30, 30, 30)):
    
    
    sgr = re.compile(r"\x1b\[([0-9:;]*)]m")

    maxLen = 0

    localBuffer = []

    for line in string.splitlines():
        localBuffer.append(list(line))
        maxLen = len(re.sub(sgr, "", line)) if maxLen < len(re.sub(sgr, "", line)) else maxLen
        
    escapeCodes = []
    finalBuffer = []

    for i, line in enumerate(localBuffer):


        
        bufferLeft = []
        bufferRight = []
        finalBuffer.append([])

        tempList = []

        for j, char in enumerate(line):
            for match in sgr.finditer(string):
                if match.group(0) == "\x1b\[0m":
                    escapeCodes = []

                else:
                    escapeCodes.append(match)

            if len(re.sub(sgr, "", char)) == 0:
                tempList.append(Cell(char, fg, bg, escapeCodes if len(escapeCodes) > 0 else ["\x1b\[0m"]))

        finalBuffer.append(tempList)

    return finalBuffer

term = Terminal()

defaultColorFront = (212, 212, 212)
defualtColorBack = (30, 30, 30)
defaultCell = Cell(" ", defaultColorFront, defualtColorBack)

print(term.color_rgb(*defaultColorFront) + term.on_color_rgb(*defualtColorBack))


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
    "button1" : Button(Vector2(0, 0) + drawArea, "Hello\nWorld!", Vector2(firmsArea.x, math.floor(firmsArea.y/firms)), clickable=True),
    "button2" : Button(Vector2(0, firmsArea.y//firms * 1) + drawArea, "A clickable\nbutton", Vector2(firmsArea.x, math.floor(firmsArea.y/firms))),
    "button3" : Button(Vector2(0, firmsArea.y//firms * 2) + drawArea, "A third\nclickable button", Vector2(firmsArea.x, math.floor(firmsArea.y/firms)), clickable = True),
    "newspaper" : Button(newspaperPos, "\033[1mTODAYS NEWS:\033[0m\n\nA woman has fallen down\na stair. Oh no!\n" + "-"*(newspaperSize.x-2) + "\nI shit my pants.\nThis WILL affect the market.", newspaperSize, colorBack = Vector([239, 230, 210]), colorFront=Vector([28, 26, 23]))
}


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

            renderScreen(term, screenBuffer)

            framecount += 1


print(term.move_xy(0, drawArea.y+8) + "Hello")
for i in range(term.height):
    print(term.move_xy(0, drawArea.y + i + 1) + " "*term.width, end="", flush=True)

print(term.move_xy(startPos.x, startPos.y))