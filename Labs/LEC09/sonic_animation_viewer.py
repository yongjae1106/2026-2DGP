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

# 카메라 기준점: 캐릭터 발 위치. ZOOM을 바꿔도 이 점은 화면에서 안 움직임
CHAR_X = 400
GROUND_Y = 52

BASE_CHAR_SCALE = 5   # 캐릭터 픽셀아트 기본 확대 배율
ZOOM = 2               # 창 크기(800x600)는 그대로 두고, 보이는 장면 전체를 확대하는 배율
SKY_COLOR = (135, 206, 235)

def zoom_pos(x, y):
    return CHAR_X + (x - CHAR_X) * ZOOM, GROUND_Y + (y - GROUND_Y) * ZOOM

def zoom_size(w, h):
    return w * ZOOM, h * ZOOM

def draw_frame(frame, hold=0.1):
    # 발(프레임 아래쪽)을 GROUND_Y에 고정해서, 동작마다 프레임 높이가
    # 달라도 캐릭터가 위아래로 흔들리지 않게 함
    left, bottom, width, height = frame
    char_scale = BASE_CHAR_SCALE * ZOOM
    w, h = width * char_scale, height * char_scale
    clear_canvas()
    draw_rectangle(0, 0, 800, 600, *SKY_COLOR, filled=True)
    grass_x, grass_y = zoom_pos(400, 30)
    grass.draw(grass_x, grass_y, *zoom_size(grass.w, grass.h))
    sonic.clip_draw_to_origin(left, bottom, width, height, CHAR_X - w / 2, GROUND_Y, w, h)
    update_canvas()
    delay(hold)

def play_animation(frames, repeats=5, hold=1.0):
    for _ in range(repeats):
        for frame in frames:
            check_quit()
            if quit_requested:
                return
            draw_frame(frame)
    draw_frame(frames[-1], hold=hold)

def action_walk():
    play_animation(WALK_FRAMES)

# sonic-sprite.png의 달리기(Run) 행 (y 79~117, 12프레임)
RUN_FRAMES = [
    (8, 407, 26, 39),
    (37, 407, 27, 39),
    (65, 407, 31, 39),
    (97, 407, 37, 39),
    (135, 407, 32, 39),
    (170, 407, 32, 39),
    (206, 407, 26, 39),
    (238, 407, 24, 39),
    (263, 407, 30, 39),
    (295, 407, 36, 39),
    (334, 407, 32, 39),
    (370, 407, 29, 39),
]

def action_run():
    play_animation(RUN_FRAMES)

# sonic-sprite.png의 구르기(Roll) 행 (y 206~232, 6프레임)
ROLL_FRAMES = [
    (1, 292, 30, 27),
    (36, 292, 29, 27),
    (70, 292, 29, 27),
    (105, 292, 29, 27),
    (139, 292, 29, 27),
    (174, 292, 29, 27),
]

def action_roll():
    play_animation(ROLL_FRAMES)

# sonic-sprite.png의 아이들(Idle, 뒤돌아보기) 행 (y 326~370, 8프레임)
IDLE_FRAMES = [
    (1, 154, 24, 45),
    (31, 154, 29, 45),
    (65, 154, 20, 45),
    (90, 154, 25, 45),
    (119, 154, 25, 45),
    (149, 154, 20, 45),
    (184, 154, 40, 45),
    (232, 154, 39, 45),
]

def action_idle():
    play_animation(IDLE_FRAMES)

# sonic-sprite.png의 브레이크(Skid) 행 (y 121~163, 6프레임)
SKID_FRAMES = [
    (1, 361, 33, 43),
    (39, 361, 35, 43),
    (89, 361, 35, 43),
    (130, 361, 34, 43),
    (181, 361, 34, 43),
    (228, 361, 33, 43),
]

def action_skid():
    play_animation(SKID_FRAMES)

# sonic-sprite.png의 발 구르기(Tap, 조급해하는 아이들) 행 (y 426~468, 4프레임)
TAP_FRAMES = [
    (6, 56, 34, 43),
    (49, 56, 34, 43),
    (96, 56, 23, 43),
    (125, 56, 23, 43),
]

def action_tap():
    play_animation(TAP_FRAMES)

while not quit_requested:
    action_walk()
    action_run()
    action_roll()
    action_idle()
    action_skid()
    action_tap()

close_canvas()
