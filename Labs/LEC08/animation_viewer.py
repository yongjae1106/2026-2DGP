from pico2d import *

open_canvas(800, 600)
hide_lattice()
grass = load_image('grass.png')
character = load_image('character.png')

quit_requested = False

# 카메라 기준점: 캐릭터 발 위치. ZOOM을 아무리 바꿔도 이 점은 화면에서 안 움직임
CHAR_X = 400
GROUND_Y = 52

BASE_CHAR_SCALE = 5   # 캐릭터 픽셀아트 기본 확대 배율
ZOOM = 5               # 창 크기(800x600)는 그대로 두고, 보이는 장면 전체를 확대하는 배율
REPEATS = 5
HOLD_SECONDS = 1.0
SKY_COLOR = (135, 206, 235)

def zoom_pos(x, y):
    # CHAR_X, GROUND_Y(카메라 기준점)로부터 얼마나 떨어져 있는지를 ZOOM배 늘려서,
    # 기준점은 고정한 채 나머지가 기준점 중심으로 확대되게 함
    return CHAR_X + (x - CHAR_X) * ZOOM, GROUND_Y + (y - GROUND_Y) * ZOOM

def zoom_size(w, h):
    return w * ZOOM, h * ZOOM

def check_quit():
    global quit_requested
    for event in get_events():
        if event.type == SDL_QUIT:
            quit_requested = True
            
def draw_frame(frame, hold=0.1):
    # 프레임마다 가로폭(width)은 포즈에 따라 다르고(같은 동작 안에서도),
    # 동작 사이에는 세로높이(height)도 다름(특히 ATTACK_FRAMES).
    # 발(프레임 아래쪽)을 GROUND_Y에 고정해서, 높이가 달라도
    # 캐릭터가 위아래로 흔들리지 않게 함
    left, bottom, width, height = frame
    char_scale = BASE_CHAR_SCALE * ZOOM
    w, h = width * char_scale, height * char_scale
    clear_canvas()
    draw_rectangle(0, 0, 800, 600, *SKY_COLOR, filled=True)

    grass_x, grass_y = zoom_pos(400, 30)
    grass.draw(grass_x, grass_y, *zoom_size(grass.w, grass.h))
    character.clip_draw_to_origin(left, bottom, width, height, CHAR_X - w / 2, GROUND_Y, w, h)
    update_canvas()
    delay(hold)

def play_animation(frames, repeats=REPEATS, hold=HOLD_SECONDS):
    for _ in range(repeats):
        for frame in frames:
            check_quit()
            if quit_requested:
                return
            draw_frame(frame)
    draw_frame(frames[-1], hold=hold)

# character.png의 "Walking" 행 (y 55~73, 왼쪽부터 10프레임)
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
    play_animation(WALK_FRAMES)

# character.png의 "Running then Skid" 행 (y 78~97, 멈추는 마지막 프레임은 제외)
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
    play_animation(RUN_FRAMES)

# character.png의 "Jumping/Landing" 행 (y 102~121, 첫 프레임은 픽셀이 붙어있어 수동으로 잘라냄)
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
    play_animation(JUMP_FRAMES)

# character.png의 "Attacks" 첫 번째 행 (y 190~222, "Attacks" 텍스트 라벨은 제외)
# 이펙트(모션선/찌르기)가 위로 뻗어있어서 다른 동작(height 19~20)보다 훨씬 큼(height 33)
# -> draw_frame()에서 발 위치를 GROUND_Y로 고정해서 이 높이차 때문에 캐릭터가
#    아래로 내려가 보이는 걸 방지함
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
    play_animation(ATTACK_FRAMES)

while not quit_requested:
    action_walk()
    action_run()
    action_jump()
    action_attack()
    pass

close_canvas()
