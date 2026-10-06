from pico2d import *

open_canvas(800, 600)
hide_lattice()
grass = load_image('grass.png')
sonic = load_image('sonic-sprite.png')

quit_requested = False

def check_quit():
    global quit_requested
    for event in get_events():
        if event.type == SDL_QUIT:
            quit_requested = True

# sonic-sprite.png의 걷기(Walk) 행 (y 39~77, 11프레임)
WALK_FRAMES = [
    (1, 447, 29, 39),
    (31, 447, 26, 39),
    (58, 447, 25, 39),
    (83, 447, 33, 39),
    (118, 447, 30, 39),
    (150, 447, 30, 39),
    (182, 447, 29, 39),
    (211, 447, 29, 39),
    (240, 447, 29, 39),
    (270, 447, 24, 39),
    (302, 447, 29, 39),
]

while not quit_requested:
    check_quit()

close_canvas()
