from pico2d import *
import math

open_canvas(800, 600)
grass = load_image('grass.png')
character = load_image('character.png')

CHAR_X = 400
GROUND_Y = 52
SCALE = 4

def draw_frame(frame):
    # 발(프레임 아래쪽)을 GROUND_Y에 고정해서, 프레임 높이가 달라도(공격 이펙트 등)
    # 캐릭터가 위아래로 흔들리지 않게 함
    left, bottom, width, height = frame
    w, h = width * SCALE, height * SCALE
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw_to_origin(left, bottom, width, height, CHAR_X - w / 2, GROUND_Y, w, h)
    update_canvas()
    delay(0.1)

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
    for frame in WALK_FRAMES:
        draw_frame(frame)

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
    for frame in RUN_FRAMES:
        draw_frame(frame)

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
    for frame in JUMP_FRAMES:
        draw_frame(frame)

ATTACK_FRAMES = [
    (64, 424, 24, 33),
    (91, 424, 21, 33),
    (117, 424, 21, 33),
    (144, 424, 37, 33),
    (186, 424, 28, 33),
    (225, 424, 23, 33),
    (255, 424, 22, 33),
    (283, 424, 23, 33),
    (312, 424, 20, 33),
    (340, 424, 19, 33),
    (367, 424, 27, 33),
    (400, 424, 23, 33),
    (433, 424, 21, 33),
    (461, 424, 21, 33),
]

def action_attack():
    for frame in ATTACK_FRAMES:
        draw_frame(frame)

while True:
    action_walk()
    action_run()
    action_jump()
    action_attack()
    pass

close_canvas()
