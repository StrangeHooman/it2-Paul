import sys
from blessed import Terminal


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


class ui:
    displayList: list
    pos = Vector2(0, 0)
    size = Vector2(0, 0)
    colorFront = (212, 212, 212)
    colorBack = (30, 30, 30)

    def __init__(self, pos: Vector2, size: Vector2, displayList: list):
        self.pos = pos
        self.size = size
        self.displayList = displayList

    def render(self, terminal: Terminal):

        style = terminal.color_rgb(*self.colorFront) + terminal.on_color_rgb(*self.colorBack)
        for row, line in enumerate(self.displayList):
            print(terminal.move_xy(self.pos.x, self.pos.y + row) + style + line + terminal.normal, end="", flush=True)




class button(ui):
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




for i in range(6):
    print("\n")


term = Terminal()

clickable = []

drawArea = Vector2(0, term.height - 10)

print(term.move_xy(drawArea.x, drawArea.y) + term.width*BOX_LIGHT["h"])

button1 = button(Vector2(5, 2) + drawArea, "Hello\nWorld!")

clickable.append(button1)


button1.render(term)

if not term.does_mouse(report_motion=True):
    print("This terminal doesn't support mouse-motion reporting.")
else:
    with term.cbreak(), term.hidden_cursor(), term.mouse_enabled(report_motion=True):
        while True:
            event = term.inkey(timeout=1/60)

            if event.lower() == "q":
                break

            if event.name and event.name.startswith("MOUSE_"):
                x, y = event.mouse_xy
                button1.pos = Vector2(x, y)
                button1.render(term)
                
                for i in range(10):
                    print(term.move_xy(0, drawArea.y + i) + "")

                print(term.move_xy(0, drawArea.y + 8) + term.clear_eol
                      + f"{event.name} at x={x}, y={y}", end="", flush=True)


with term.cbreak(), term.hidden_cursor():
    inp = term.inkey()


print(term.move_xy(0, drawArea.y+8) + "Hello\n")