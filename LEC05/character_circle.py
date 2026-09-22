from pico2d import *
import math

open_canvas(800, 600)
grass = load_image('grass.png')
character = load_image('character.png')

CENTER_X, CENTER_Y = 400, 300
RADIUS = 150
ANGLE_SPEED = 0.05

angle = 0

running = True
while running:
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False

    angle += ANGLE_SPEED
    if angle >= 2 * math.pi:
        angle -= 2 * math.pi

    x = CENTER_X + RADIUS * math.cos(angle)
    y = CENTER_Y + RADIUS * math.sin(angle)

    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()
    delay(0.01)

close_canvas()
