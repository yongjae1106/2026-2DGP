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

CHAR_X = 400
GROUND_Y = 52
SCALE = 5

def draw_frame(frame, hold=0.1):
    # 발(프레임 아래쪽)을 GROUND_Y에 고정해서, 동작마다 프레임 높이가
    # 달라도 캐릭터가 위아래로 흔들리지 않게 함
    left, bottom, width, height = frame
    w, h = width * SCALE, height * SCALE
    clear_canvas()
    grass.draw(400, 30)
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

while not quit_requested:
    action_walk()

close_canvas()
