from pico2d import *
import math

open_canvas(800, 600)
grass = load_image('grass.png')
character = load_image('character.png')

quit_requested = False

def move_circle():
    print("Move Circle")
    pass
    
def move_square():
    print("Move Square")
    pass
    
def move_triangle():
    print("Move Triangle")
    pass
  
  
while not quit_requested:
    move_circle()
    if quit_requested:
        break
    move_square()
    if quit_requested:
        break
    move_triangle()
  
close_canvas()
