from blessed import Terminal

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

    def __add__(self, other: Vector2):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector2):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector2):
        return Vector2(self.x * other.x, self.y * other.y)

    def __truediv__(self, other: Vector2):
        return Vector2(self.x / other.x, self.y / other.y)

    
class UI:
    displayList: list
    pos = Vector2(0, 0)
    size = Vector2(0, 0)
    colorFront = (212, 212, 212)
    colorBack = (30, 30, 30)

    def __init__(self, pos: Vector2, size: Vector2, displayList: list):
        self.pos = pos
        self.size = size
        self.displayList = displayList

    def render(self, terminal: Terminal, buffer):

        localBuffer = []
        for i in range(len(buffer)):
            localBuffer.append(list(buffer[i]))

        localDisplayList = []
        for i in range(len(self.displayList)):
            localDisplayList.append(list(self.displayList[i]))
    

        style = terminal.color_rgb(*self.colorFront) + terminal.on_color_rgb(*self.colorBack)
        for row, string in enumerate(localDisplayList):
            for i, char in enumerate(string):
                if char != "\n":
                    localBuffer[row+self.pos.y][i+self.pos.x] = localDisplayList[row][i]
        
        return ["".join(stringList) for stringList in localBuffer]

class button(UI):
    def __init__(self, pos: Vector2, text: str):
        lines = text.splitlines()
        maxLen = 0
        for line in lines:
            if len(line) > maxLen:
                maxLen = len(line)



        self.text = text

        display = [BOX_LIGHT["tl"] + BOX_LIGHT["h"]*maxLen + BOX_LIGHT["tr"]]
        for line in lines:
            display.append(BOX_LIGHT["v"] + " "*((maxLen-len(line))//2) + line + " "*-(-(maxLen-len(line))//2) + BOX_LIGHT["v"])

        display.append(BOX_LIGHT["bl"] + BOX_LIGHT["h"]*maxLen + BOX_LIGHT["br"])

        super().__init__(pos, Vector2(2+maxLen, 2+len(lines)), display)


class text(UI):
    def __init__(self, pos: Vector2, text: str):
        super().__init__(pos, Vector2(len(text), 1), [text])

    def setText(self, text: str):
        super().size = Vector2(len(text), 1)
        super().displayList = [text]