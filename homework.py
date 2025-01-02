import pgzrun

WIDTH = 600
HEIGHT = 600

def draw():
    screen.clear()
    screen.fill("black")
    x = WIDTH // 2
    y = HEIGHT // 2
    step = 10
    max_lines = 30

    for i in range(max_lines):
        color = (255 - i * 8, 0, 255 - i * 8)
        screen.draw.line((x - i * step, y), (x, y - i * step), color)
        screen.draw.line((x + i * step, y), (x, y - i * step), color)
        screen.draw.line((x - i * step, y), (x, y + i * step), color)
        screen.draw.line((x + i * step, y), (x, y + i * step), color)

pgzrun.go()
