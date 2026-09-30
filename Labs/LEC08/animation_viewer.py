from pico2d import *
import math

open_canvas(800, 600)
grass = load_image('grass.png')
character = load_image('character.png')

def action_walk():
    print("Walking...")
    pass
def action_run():
    print("Running...")
    pass
def action_jump():
    print("Jumping...")
    pass
def action_attack():
    print("Attacking...")
    pass

while True:
    action_walk()
    action_run()
    action_jump()
    action_attack()
    pass

close_canvas()