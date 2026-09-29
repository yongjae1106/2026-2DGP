from pico2d import *
import math

open_canvas(800, 600)
grass = load_image('grass.png')
character = load_image('character.png')

quit_requested = False

def draw_render(x, y):
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()
    delay(0.01)
    
def check_quit():
    global quit_requested
    for event in get_events():
        if event.type == SDL_QUIT:
            quit_requested = True

def move_circle(SPEED):
    CENTER_X, CENTER_Y = 400, 300
    RADIUS = 200
    ANGLE_SPEED = 0.05 * SPEED
    
    angle = 0
    
    running = True
    while running:
        check_quit()
        if quit_requested:
            break

        angle += ANGLE_SPEED
        if abs(angle) >= 2 * math.pi:
            break
        
        x = CENTER_X + RADIUS * math.cos(angle)
        y = CENTER_Y + RADIUS * math.sin(angle)
        
        draw_render(x, y)
    
    print("Move Circle")
    pass

def move_square(dir):

    LEFT_X, RIGHT_X = 150, 650
    BOTTOM_Y, TOP_Y = 100, 500
    SQUARE_SPEED = 10

    vertices = [
        (LEFT_X, BOTTOM_Y),
        (RIGHT_X, BOTTOM_Y),
        (RIGHT_X, TOP_Y),
        (LEFT_X, TOP_Y),
    ]

    x, y = vertices[0]
    target_index = dir % 4

    Running = True
    while Running == True:
        check_quit()
        if quit_requested:
            break

        tx, ty = vertices[target_index]
        dx, dy = tx - x, ty - y
        dist = math.hypot(dx, dy)

        if dist <= SQUARE_SPEED:
            x, y = tx, ty
            reached_index = target_index
            target_index = (target_index + dir) % 4
            if reached_index == 0:
                Running = False
        else:
            x += dx / dist * SQUARE_SPEED
            y += dy / dist * SQUARE_SPEED

        draw_render(x, y)

    print("Move Square")
    pass

def move_triangle(dir):
    CENTER_X, CENTER_Y = 400, 220
    RADIUS = 250
    SPEED = 10

    # 정삼각형의 세 꼭짓점을 중심에서 120도씩 떨어진 각도로 계산
    vertices = []
    for i in range(3):
        angle = math.radians(90 + i * 120)
        vx = CENTER_X + RADIUS * math.cos(angle)
        vy = CENTER_Y + RADIUS * math.sin(angle)
        vertices.append((vx, vy))

    x, y = vertices[0]
    target_index = dir % 3

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
            target_index = (target_index + dir) % 3
            if reached_index == 0:
                running = False
        else:
            x += dx / dist * SPEED
            y += dy / dist * SPEED

        draw_render(x, y)
    print("Move Triangle")
    pass

dir = 1

while not quit_requested:
    move_circle(dir)
    if quit_requested:
        break
    move_square(dir)
    if quit_requested:
        break
    move_triangle(dir)
    dir *= -1

close_canvas() 
