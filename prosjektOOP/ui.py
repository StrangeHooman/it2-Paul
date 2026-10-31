from blessed import terminal


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