from pico2d import load_image, get_time, SDL_KEYDOWN, SDLK_SPACE
from transitions import Machine


class Boy:
    # 상태 목록 - IDLE 에 들어갈 때마다 5초 타이머를 시작한다
    states = [
        {'name': 'IDLE', 'on_enter': 'start_idle_timer'},
        'SLEEP',
    ]

    # 전이 목록
    transitions = [
        {'trigger': 'time_out', 'source': 'IDLE', 'dest': 'SLEEP'},
        {'trigger': 'space_down', 'source': 'SLEEP', 'dest': 'IDLE'},
    ]

    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.face_dir = 1
        self.image = load_image('animation_sheet.png')

        # transitions 상태 머신: self(Boy)가 모델이 되어 self.state 로 현재 상태를 가진다
        # ignore_invalid_triggers: 현재 상태에서 정의되지 않은 이벤트는 무시 (예: IDLE 에서 SPACE)
        self.machine = Machine(model=self, states=Boy.states, transitions=Boy.transitions,
                               initial='IDLE', ignore_invalid_triggers=True)
        # 초기 상태 진입 시에는 on_enter 가 호출되지 않으므로 직접 타이머 시작
        self.start_idle_timer()

    def start_idle_timer(self):
        self.idle_start_time = get_time()

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            self.space_down()

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.state == 'IDLE' and get_time() - self.idle_start_time >= 5:
            self.time_out()

    def draw(self):
        if self.state == 'IDLE':
            if self.face_dir == 1:
                self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
            else:
                self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        elif self.state == 'SLEEP':
            # IDLE 프레임을 90도 눕혀서 그린다
            if self.face_dir == 1:
                self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                               3.141592 / 2, '', self.x - 25, self.y - 25, 100, 100)
            else:
                self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                               -3.141592 / 2, '', self.x + 25, self.y - 25, 100, 100)
