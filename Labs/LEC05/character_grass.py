from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

x = 0
game_is_running = True

def update_game_logic():
    global x, game_is_running
    x += 2
    if x > 800:
        game_is_running = False

def render_game_state():
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, 90)
    update_canvas()

while game_is_running:
    update_game_logic()
    render_game_state()
    delay(0.01)

close_canvas()
