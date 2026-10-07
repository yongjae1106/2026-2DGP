# 소닉 애니메이션 뷰어
# sonic-sprite.png에서 동작별(걷기/달리기/구르기/아이들/브레이크/발구르기)
# 프레임을 잘라 순서대로 재생한다. 각 동작은 5회 반복 후 1초 정지하고
# 다음 동작으로 넘어가며, 모든 동작을 다 돌면 처음부터 다시 반복한다.
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

# sonic-sprite.png의 걷기(Walk) 행 (y 79~117, 12프레임)
# 0.1초 간격 기준 한 바퀴 1.2초라 걷는 속도로 보임
WALK_FRAMES = [
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

# 카메라 기준점: 캐릭터 발 위치. ZOOM을 바꿔도 이 점은 화면에서 안 움직임
CHAR_X = 400
GROUND_Y = 52

BASE_CHAR_SCALE = 5   # 캐릭터 픽셀아트 기본 확대 배율
ZOOM = 1               # 창 크기(800x600)는 그대로 두고, 보이는 장면 전체를 확대하는 배율
SKY_COLOR = (135, 206, 235)

def zoom_pos(x, y):
    return CHAR_X + (x - CHAR_X) * ZOOM, GROUND_Y + (y - GROUND_Y) * ZOOM

def zoom_size(w, h):
    return w * ZOOM, h * ZOOM

# 이동하는 동작(걷기/달리기/구르기)에서 캐릭터가 왼쪽에서 오른쪽으로 움직이는 범위.
# 배경(잔디)은 CHAR_X 기준으로 고정돼있고, 캐릭터만 그 위를 왼쪽->오른쪽으로 지나간다.
MOVE_LEFT_X = 150
MOVE_RIGHT_X = 650
MOVE_SPEED = 15     # 걷기/구르기 기본 이동 속도
RUN_MOVE_SPEED = 30  # 달리기는 더 빠르게
char_x = CHAR_X

def draw_frame(frame, hold=0.1, moving=False, speed=MOVE_SPEED):
    # 발(프레임 아래쪽)을 GROUND_Y에 고정해서, 동작마다 프레임 높이가
    # 달라도 캐릭터가 위아래로 흔들리지 않게 함
    global char_x
    left, bottom, width, height = frame
    char_scale = BASE_CHAR_SCALE * ZOOM
    w, h = width * char_scale, height * char_scale

    if moving:
        char_x = min(char_x + speed, MOVE_RIGHT_X)

    clear_canvas()
    draw_rectangle(0, 0, 800, 600, *SKY_COLOR, filled=True)
    grass_x, grass_y = zoom_pos(400, 30)
    grass.draw(grass_x, grass_y, *zoom_size(grass.w, grass.h))
    sonic.clip_draw_to_origin(left, bottom, width, height, char_x - w / 2, GROUND_Y, w, h)
    update_canvas()
    delay(hold)

def play_animation(frames, repeats=5, hold=1.0, moving=False, speed=MOVE_SPEED):
    global char_x
    for _ in range(repeats):
        char_x = MOVE_LEFT_X  # 한 바퀴(repeat) 끝날 때마다 다시 원래 자리에서 시작
        for frame in frames:
            check_quit()
            if quit_requested:
                return
            draw_frame(frame, moving=moving, speed=speed)
    draw_frame(frames[-1], hold=hold, moving=False)

def action_walk():
    play_animation(WALK_FRAMES, moving=True)

# 달리기(Run) 루프 = 6행 1~6열 + 7행 3~6열
RUN_FRAMES = [
    # 6행 (y 238~273)
    (1, 251, 29, 36),
    (36, 251, 30, 36),
    (74, 251, 31, 36),
    (111, 251, 31, 36),
    (149, 251, 30, 36),
    (186, 251, 31, 36),
    # 7행 (y 283~317) 3~6열
    (72, 207, 39, 35),
    (123, 207, 39, 35),
    (172, 207, 39, 35),
    (218, 207, 38, 35),
    (72, 207, 39, 35),
    (123, 207, 39, 35),
    (172, 207, 39, 35),
    (218, 207, 38, 35),
    (72, 207, 39, 35),
    (123, 207, 39, 35),
    (172, 207, 39, 35),
    (218, 207, 38, 35),
]

def action_run():
    play_animation(RUN_FRAMES, moving=True, speed=RUN_MOVE_SPEED)

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
    play_animation(ROLL_FRAMES, moving=True)

# sonic-sprite.png의 아이들(Idle, 뒤돌아보기) 행 (y 326~370, 6프레임)
# 뒤쪽 2프레임은 같은 행이지만 다른 포즈(놀라서 돌아보기)라서 제외함
IDLE_FRAMES = [
    (1, 154, 24, 45),
    (31, 154, 29, 45),
    (65, 154, 20, 45),
    (90, 154, 25, 45),
    (119, 154, 25, 45),
    (149, 154, 20, 45),
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
    action_roll()
    action_idle()
    action_run()
    action_skid()
    action_tap()
    
close_canvas()
