from blessed import Terminal
from ui import *
import time



def clearBuffer(term: Terminal):
    buffer = []
    for i in range(term.height):
        buffer.append(" "*term.width)

    return buffer

def renderScreen(term: Terminal, buffer):
    for i, str in enumerate(buffer):
        print(term.move_xy(0, 1*i) + str, end="", flush=True)



term = Terminal()

defaultColorFront = (212, 212, 212)
defualtColorBack = (30, 30, 30)


print(term.color_rgb(*defaultColorFront) + term.on_color_rgb(*defualtColorBack))


screenBuffer = []

for i in range (term.height):
    screenBuffer.append(" "*term.width)

renderScreen(term, screenBuffer)



startPos = Vector2(*term.get_location())

clickable = []

drawArea = Vector2(0, 0)

print(term.move_xy(drawArea.x, drawArea.y) + term.width*BOX_LIGHT["h"])

button1 = button(Vector2(0, 1) + drawArea, "Hello\nWorld!")
button2 = button(Vector2(0, 6) + drawArea, "A clickable\nbutton")
text1 = text(Vector2(0, 10), "Hello!")

clickable.append(button1)


screenBuffer = button1.render(term, screenBuffer)
ScreenBuffer = text1.render(term, screenBuffer)

if not term.does_mouse(report_motion=True):
    print("This terminal doesn't support mouse-motion reporting.")
else:
    with term.cbreak(), term.hidden_cursor(), term.mouse_enabled(report_motion=True):
        while True:
            event = term.inkey(timeout=1/60)

            screenBuffer = clearBuffer(term)

            if event.lower() == "q":
                break

            if event.name and event.name.startswith("MOUSE_"):
                x, y = event.mouse_xy



                #print(term.move_xy(0, drawArea.y + 15) + term.clear_eol + f"{event.name} at x={x}, y={y}", end="", flush=True)
                text1 = text(text1.pos, text1.displayList[0])

                button1.pos = Vector2(x, y) + drawArea
            button2.pos = Vector2(0, 6) + drawArea
            screenBuffer = text1.render(term, screenBuffer)
            screenBuffer = button1.render(term, screenBuffer)
            screenBuffer = button2.render(term, screenBuffer)
            renderScreen(term, screenBuffer)


print(term.move_xy(0, drawArea.y+8) + "Hello")
for i in range(term.height):
    print(term.move_xy(0, drawArea.y + i + 1) + " "*term.width, end="", flush=True)

print(term.move_xy(startPos.x, startPos.y))