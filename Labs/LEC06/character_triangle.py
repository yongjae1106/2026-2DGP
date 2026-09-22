from pico2d import *
import math

open_canvas(800, 600)
grass = load_image('grass.png')
character = load_image('character.png')

CENTER_X, CENTER_Y = 400, 300
RADIUS = 250
SPEED = 5

# 정삼각형의 세 꼭짓점을 중심에서 120도씩 떨어진 각도로 계산
vertices = []
for i in range(3):
    angle = math.radians(90 + i * 120)
    vx = CENTER_X + RADIUS * math.cos(angle)
    vy = CENTER_Y + RADIUS * math.sin(angle)
    vertices.append((vx, vy))

target_index = 1
x, y = vertices[0]

running = True
while running:
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False

    tx, ty = vertices[target_index]
    dx, dy = tx - x, ty - y
    dist = math.hypot(dx, dy)

    if dist <= SPEED:
        x, y = tx, ty
        target_index = (target_index + 1) % 3
    else:
        x += dx / dist * SPEED
        y += dy / dist * SPEED

    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()
    delay(0.01)

close_canvas()
