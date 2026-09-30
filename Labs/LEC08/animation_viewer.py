from pico2d import *
import math

open_canvas(800, 600)
grass = load_image('grass.png')
character = load_image('character.png')

WALK_FRAMES = [
    (9, 573, 21, 19),
    (34, 573, 20, 19),
    (58, 573, 19, 19),
    (81, 573, 17, 19),
    (102, 573, 17, 19),
    (123, 573, 21, 19),
    (148, 573, 20, 19),
    (172, 573, 19, 19),
    (195, 573, 19, 19),
    (218, 573, 20, 19),
]

def action_walk():
    # 3단계: 프레임을 하나씩 순회하며 그려서 걷는 모션처럼 보이게 함
    for left, bottom, width, height in WALK_FRAMES:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(left, bottom, width, height, 400, 90, width * 4, height * 4)
        update_canvas()
        delay(0.1)
    
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