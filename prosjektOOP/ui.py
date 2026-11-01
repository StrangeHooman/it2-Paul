from blessed import Terminal
import math

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
BLOCK_STEPS = {
    1: "▏",
    2: "▎",
    3: "▍",
    4: "▌",
    5: "▋",
    6: "▊",
    7: "▉",
    8: "█"
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
    def __init__(self, char, foreGround, backGround, styles):
        self.fg = foreGround
        self.bg = backGround
        self.char = char
        self.styles = styles
    
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

        localBuffer = []
        for i in range(len(buffer)):
            localBuffer.append(list(buffer[i]))

        localDisplayList = []
        for i in range(len(self.displayList)):
            localDisplayList.append(list(self.displayList[i]))
    

        foreGround = tuple((self.colorFront + self.colorFrontOffset).values)
        backGround = tuple((self.colorBack + self.colorBackOffset).values)


        for row, string in enumerate(localDisplayList):
            for i, char in enumerate(string):
                try:
                    localBuffer[row+self.pos.y][i+self.pos.x] = Cell(char, foreGround, backGround)

                except IndexError:
                    pass


        
        return localBuffer

class Button(UI):
    def __init__(self, pos: Vector2, text: str, size = Vector2(0, 0), *, clickable = False, colorFront = Vector([212, 212, 212]), colorBack = Vector([30, 30, 30])):
        

        lines = text.splitlines()
        maxLen = 0
        for line in lines:
            if len(line) > maxLen:
                maxLen = len(line)

        maxLen = max(maxLen, size.x - 2)

        self.text = text

        display = [BOX_LIGHT["tl"] + BOX_LIGHT["h"]*maxLen + BOX_LIGHT["tr"]]

        for i in range(math.floor(((size.y - 2) - len(lines))/2)):
            display.append(BOX_LIGHT["v"] + " " * maxLen + BOX_LIGHT["v"])

        for line in lines:
            display.append(BOX_LIGHT["v"] + " "*((maxLen-len(line))//2) + line + " "*-(-(maxLen-len(line))//2) + BOX_LIGHT["v"])

        for i in range(math.ceil(((size.y - 2) - len(lines))/2)):
            display.append(BOX_LIGHT["v"] + " " * maxLen + BOX_LIGHT["v"])

        display.append(BOX_LIGHT["bl"] + BOX_LIGHT["h"]*maxLen + BOX_LIGHT["br"])

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
    def __init__(self, pos: Vector2, text: str):
        super().__init__(pos, Vector2(len(text), 1), [text])

    def setText(self, text: str):
        super().size = Vector2(len(text), 1)
        super().displayList = [text]