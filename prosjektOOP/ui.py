from blessed import Terminal
import math
import re

BOX_OUTER = {
    'tl': '▛',  # \u259B Upper Left Quadrant Block
    'tr': '▜',  # \u259C Upper Right Quadrant Block
    'bl': '▙',  # \u2599 Lower Left Quadrant Block
    'br': '▟',  # \u259F Lower Right Quadrant Block
    't': '▔',   # \u2594 Upper One Eighth Block
    'b': '▁',
    'l': '▎',   # \u258F Left One Eighth Block
    'r': '🮇'  # \u2595 Right One Eighth Block (Added since sides have directional bias)
}

BOX_LIGHT = {
    'tl': '┌', 'tr': '┐', 'bl': '└', 'br': '┘', 
    'h': '─', 'v': '│', 't_dn': '┬', 't_up': '┴'
}

BOX_DOUBLE = {
    'tl': '╔', 'tr': '╗', 'bl': '╚', 'br': '╝', 
    'h': '═', 'v': '║', 't_dn': '╦', 't_up': '╩'
}

# 🧱 Block elements of varying dimensions
BLOCKS = {
    "full": "█",        # Full character box cell
    "top_half": "▀",    # Fills the top 50%
    "bottom_half": "▄", # Fills the bottom 50%
    "left_half": "▌",   # Fills the left 50%
    "right_half": "▐",  # Fills the right 50%
}

# 🏁 Smooth horizontal loading bar elements (1/8th increments)
# Excellent for fractional progress steps without jumping full grid cells

BLOCK_STEPS_L = {
    1: "▏",
    2: "▎",
    3: "▍",
    4: "▌",
    5: "▋",
    6: "▊",
    7: "▉",
    8: "█"
}

BLOCK_STEPS_R = {
    1: "\u2595",      # ▕ Right 1/8 block (Standard Block Elements)
    2: "\U0001FB87",  # 🮇 Right 1/4 block (Symbols for Legacy Computing)
    3: "\U0001FB88",  # 🮈 Right 3/8 block (Symbols for Legacy Computing)
    4: "\u2590",      # ▐ Right 1/2 block (Standard Block Elements)
    5: "\U0001FB89",  # 🮉 Right 5/8 block (Symbols for Legacy Computing)
    6: "\U0001FB8A",  # 🮊 Right 3/4 block (Symbols for Legacy Computing)
    7: "\U0001FB8B",  # 🮋 Right 7/8 block (Symbols for Legacy Computing)
    8: "\u2588",      # █ Full block (Standard Block Elements)
}

# ░ Texture shades for background depths and drop-shadows
SHADES = {
    "light": "░",   # 25% opacity
    "medium": "▒",  # 50% opacity
    "dark": "▓",    # 75% opacity
}

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if type(other) != Vector2:
            other = Vector2(other, other)

        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector2):
        if type(other) != Vector2:
            other = Vector2(other, other)

        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector2):
        if type(other) != Vector2:
            other = Vector2(other, other)

        return Vector2(self.x * other.x, self.y * other.y)

    def __truediv__(self, other: Vector2):
        if type(other) != Vector2:
            other = Vector2(other, other)

        return Vector2(self.x / other.x, self.y / other.y)

    
    def __lt__(self, other):
        if type(other) != Vector2:
            other = Vector2(other, other)

        if self.x < other.x and self.y < other.y:
            return True

        else:
            return False

    def __le__(self, other):
        if type(other) != Vector2:
            other = Vector2(other, other)

        if self.x <= other.x and self.y <= other.y:
            return True

        else:
            return False

    def __eq__(self, other):
        if type(other) != Vector2:
            other = Vector2(other, other)

        if self.x == other.x and self.y == other.y:
            return True

        else:
            return False

    def __ge__(self, other):
        if type(other) != Vector2:
            other = Vector2(other, other)

        if self.x >= other.x and self.y >= other.y:
            return True

        else:
            return False

    def __gt__(self, other):
        if type(other) != Vector2:
            other = Vector2(other, other)

        if self.x < other.x and self.y < other.y:
            return True

        else:
            return False

class Vector():
    def __init__(self, values):
        self.values = values

    def __add__(self, other):

        finalVec = [0 for i in range(len(self.values))]
        
        if type(other) == int or type(other) == float:
            finalVec = [self.values[i] + other for i in range(len(self.values))]

        elif type(other) == Vector and len(self.values) == len(other.values):
            finalVec = [self.values[i] + other.values[i] for i in range(len(self.values))]

        return Vector(finalVec)

    def __sub__(self, other):

        finalVec = [0 for i in range(len(self.values))]
        
        if type(other) == int or type(other) == float:
            finalVec = [self.values[i] - other for i in range(len(self.values))]

        elif type(other) == Vector and len(self.values) == len(other.values):
            finalVec = [self.values[i] - other.values[i] for i in range(len(self.values))]

        return Vector(finalVec)

    def __mul__(self, other):

        finalVec = [0 for i in range(len(self.values))]
        
        if type(other) == int or type(other) == float:
            finalVec = [self.values[i] * other for i in range(len(self.values))]

        elif type(other) == Vector and len(self.values) == len(other.values):
            finalVec = [self.values[i] * other.values[i] for i in range(len(self.values))]

        return Vector(finalVec)

    def __truediv__(self, other):

        finalVec = [0 for i in range(len(self.values))]
        
        if type(other) == int or type(other) == float:
            finalVec = [self.values[i] / other for i in range(len(self.values))]

        elif type(other) == Vector and len(self.values) == len(other.values):
            finalVec = [self.values[i] / other.values[i] for i in range(len(self.values))]

        return Vector(finalVec)

class Cell:
    def __init__(self, char, foreGround: Vector, backGround: Vector, styles = []):
        self.fg = foreGround
        self.bg = backGround
        self.char = char
        self.styles = styles

def textToCell(string: str, horizontalLayout = 0, *, fg = Vector([212, 212, 212]), bg = Vector([30, 30, 30])):
    emptyCell = Cell(" ", fg, bg, [])
    
    sgr = re.compile(r"\x1b\[([0-9:;]*)m")

    maxLen = 0

    localBuffer = []

    textList = string.splitlines()

    for line in textList:
        localBuffer.append(list(line))
        maxLen = len(re.sub(sgr, "", line)) if maxLen < len(re.sub(sgr, "", line)) else maxLen
        
    styles = []
    finalBuffer = []

    for i, line in enumerate(string.splitlines()):
        tempList = []
        lastPos = 0


        leftBuffer = [emptyCell for i in range(math.floor((maxLen - len(re.sub(sgr, "", line)))/2 *horizontalLayout))]
        rightBuffer = [emptyCell for i in range(math.ceil((maxLen - len(re.sub(sgr, "", line)))/2 *(2-horizontalLayout)))]

        for match in sgr.finditer(line):
            text = line[lastPos:match.start()]

            for char in text:
                tempList.append(Cell(char, fg, bg, styles.copy() if len(styles) > 0 else ["\x1b[0m"]))

            lastPos = match.end()


            if match.group(0) == "\x1b[0m":
                styles = []

            else:
                styles.append(match.group(0))



        text = line[lastPos:]

        for char in text:
            tempList.append(Cell(char, fg, bg, styles if len(styles) > 0 else ["\x1b[0m"]))


        finalBuffer.append(leftBuffer + tempList + rightBuffer)

    return finalBuffer


class UI:
    displayList: list
    pos = Vector2(0, 0)
    size = Vector2(0, 0)
    colorFront = Vector([212, 212, 212])
    colorFrontOffset = Vector([0, 0, 0])
    colorBack = Vector([30, 30, 30])
    colorBackOffset = Vector([0, 0, 0])
    

    def __init__(self, pos: Vector2, size: Vector2, displayList: list, colorFront, colorBack):
        self.pos = pos
        self.size = size
        self.displayList = displayList
        self.colorFront = colorFront
        self.colorBack = colorBack

    def render(self, terminal: Terminal, buffer):    

        for row, string in enumerate(self.displayList):
            for i, cell in enumerate(string):
                try:
                    foreGround = (cell.fg + self.colorFrontOffset)
                    backGround = (cell.bg + self.colorBackOffset)

                    buffer[row+self.pos.y][i+self.pos.x] = Cell(cell.char, foreGround, backGround, cell.styles)

                except IndexError:
                    pass


        
        return buffer

class Button(UI):
    def __init__(self, pos: Vector2, text: list, size = Vector2(0, 0), *, clickable = False, colorFront = Vector([212, 212, 212]), colorBack = Vector([30, 30, 30])):
        

        maxLen = max(len(text[0]), size.x - 2)

        self.text = text

        display = [textToCell(BOX_LIGHT["tl"] + BOX_LIGHT["h"]*maxLen + BOX_LIGHT["tr"], fg = (colorFront), bg = (colorBack))[0]]

        for i, row in enumerate(text):

            tempList = textToCell(BOX_LIGHT["v"], fg = colorFront, bg = colorBack)[0]

            for j, cell in enumerate(row):
                tempList.append(cell)

            tempList.append(textToCell(BOX_LIGHT["v"], fg = colorFront, bg = colorBack)[0][0])

            display.append(tempList)

        display.append(textToCell(BOX_LIGHT["bl"] + BOX_LIGHT["h"]*maxLen + BOX_LIGHT["br"], fg = (colorFront), bg = (colorBack))[0])

        self.clickable = clickable

        super().__init__(pos, Vector2(2+maxLen, len(display)), display, colorFront, colorBack)




    def clicked(self, mousepos: Vector2, clicked = False, function = None, funcArgs: tuple = None):
        inside =  True if (mousepos >= self.pos) and (mousepos < (self.size + self.pos)) else False

        if inside and self.clickable:
            self.colorBackOffset = self.colorBack * 1

            if clicked:
                function(*funcArgs)

        else:
            self.colorBackOffset = self.colorBack * 0




class Text(UI):
    def __init__(self, pos: Vector2, text: list):
        maxLen = len(text[0])
        super().__init__(pos, Vector2(maxLen, len(text)), text, Vector([100, 100, 100]), Vector([100, 100, 100]))

    def setText(self, text: list):
        super().size = Vector2(len(text[0]), len(text))
        super().displayList = text

defaultColorFront = Vector([212, 212, 212])
defualtColorBack = Vector([30, 30, 30])
defaultCell = Cell(" ", defaultColorFront, defualtColorBack, [])