from pico2d import load_image
from transitions import Machine


class Boy:
    # 상태 목록 - 지금은 IDLE 하나뿐
    states = ['IDLE']

    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.face_dir = 1
        self.image = load_image('animation_sheet.png')

        # transitions 상태 머신: self(Boy)가 모델이 되어 self.state 로 현재 상태를 가진다
        self.machine = Machine(model=self, states=Boy.states, initial='IDLE')

    def update(self):
        if self.state == 'IDLE':
            self.frame = (self.frame + 1) % 8

    def draw(self):
        if self.state == 'IDLE':
            if self.face_dir == 1:
                self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
            else:
                self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
