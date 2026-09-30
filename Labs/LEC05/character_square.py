from pico2d import *

open_canvas(800, 600)
grass = load_image('grass.png')
character = load_image('character.png')

LEFT_X, RIGHT_X = 150, 650
BOTTOM_Y, TOP_Y = 100, 500
SPEED = 5

RIGHT, UP, LEFT, DOWN = range(4)

x, y = LEFT_X, BOTTOM_Y
direction = RIGHT

running = True
while running:
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False

    if direction == RIGHT:
        x += SPEED
        if x >= RIGHT_X:
            x = RIGHT_X
            direction = UP
    elif direction == UP:
        y += SPEED
        if y >= TOP_Y:
            y = TOP_Y
            direction = LEFT
    elif direction == LEFT:
        x -= SPEED
        if x <= LEFT_X:
            x = LEFT_X
            direction = DOWN
    elif direction == DOWN:
        y -= SPEED
        if y <= BOTTOM_Y:
            y = BOTTOM_Y
            direction = RIGHT

    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()
    delay(0.01)

close_canvas()
