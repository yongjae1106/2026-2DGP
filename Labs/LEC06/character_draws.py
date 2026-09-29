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

def move_circle():
    CENTER_X, CENTER_Y = 400, 300
    RADIUS = 130
    ANGLE_SPEED = 0.08
    
    angle = 0
    
    running = True
    while running:
        angle += ANGLE_SPEED
        if angle >= 2 * math.pi:
            break
        
        x = CENTER_X + RADIUS * math.cos(angle)
        y = CENTER_Y + RADIUS * math.sin(angle)
        
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        delay(0.01)
    
    print("Move Circle")
    pass

def move_square():
    print("Move Square")
    pass

def move_triangle():
    print("Move Triangle")
    pass

while True:
    move_circle()
    move_square()
    move_triangle()


close_canvas() 
