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
    
RUN_FRAMES = [
    (9, 549, 19, 20),
    (32, 549, 18, 20),
    (54, 549, 17, 20),
    (75, 549, 19, 20),
    (98, 549, 24, 20),
    (126, 549, 19, 20),
    (149, 549, 17, 20),
    (170, 549, 18, 20),
]

def action_run():
    for left, bottom, width, height in RUN_FRAMES:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(left, bottom, width, height, 400, 90, width * 4, height * 4)
        update_canvas()
        delay(0.1)
JUMP_FRAMES = [
    (10, 525, 20, 20),
    (30, 525, 21, 20),
    (55, 525, 20, 20),
    (79, 525, 21, 20),
    (104, 525, 20, 20),
    (128, 525, 21, 20),
    (153, 525, 22, 20),
    (179, 525, 21, 20),
    (204, 525, 20, 20),
]

def action_jump():
    for left, bottom, width, height in JUMP_FRAMES:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(left, bottom, width, height, 400, 90, width * 4, height * 4)
        update_canvas()
        delay(0.1)
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