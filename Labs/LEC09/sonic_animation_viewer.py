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

while not quit_requested:
    check_quit()

close_canvas()
