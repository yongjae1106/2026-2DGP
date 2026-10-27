from pico2d import *
import random


class Boy:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(0, 800), 90
        self.frame = random.randint(0, 7)
        if Boy.image is None:
            Boy.image = load_image('run_animation.png')
        self.image = Boy.image

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
