from pico2d import *
import math

open_canvas(800, 600)
grass = load_image('grass.png')
character = load_image('character.png')

quit_requested = False

def check_quit():
    global quit_requested
    for event in get_events():
        if event.type == SDL_QUIT:
            quit_requested = True

def move_circles():
    CENTER_X, CENTER_Y = 400, 300
    RADIUS = 150
    ANGLE_SPEED = 0.05

    angle = 0

    running = True
    while running:
        check_quit()
        if quit_requested:
            break

        angle += ANGLE_SPEED
        if angle >= 2 * math.pi:
            running = False

        x = CENTER_X + RADIUS * math.cos(angle)
        y = CENTER_Y + RADIUS * math.sin(angle)

        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        delay(0.01)

    print ("Circle")
    pass

def move_rectangles():
    LEFT_X, RIGHT_X = 150, 650
    BOTTOM_Y, TOP_Y = 100, 500
    SPEED = 5

    RIGHT, UP, LEFT, DOWN = range(4)

    x, y = LEFT_X, BOTTOM_Y
    direction = RIGHT
    
    Running = True
    while Running == True:
        check_quit()
        if quit_requested:
            break

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
                Running = False
        
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        delay(0.01)
    
    print("Rectangle")
    pass

def move_triangles():
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
        check_quit()
        if quit_requested:
            break

        tx, ty = vertices[target_index]
        dx, dy = tx - x, ty - y
        dist = math.hypot(dx, dy)

        if dist <= SPEED:
            x, y = tx, ty
            reached_index = target_index
            target_index = (target_index + 1) % 3
            if reached_index == 0:
                running = False
        else:
            x += dx / dist * SPEED
            y += dy / dist * SPEED

        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        delay(0.01)
    
    print("Triangle")
    pass

while not quit_requested:
    move_circles()
    if quit_requested:
        break
    move_rectangles()
    if quit_requested:
        break
    move_triangles()

close_canvas()

