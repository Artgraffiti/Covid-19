from pygame.sprite import Sprite
from random import randint


class Human(Sprite):
    def __init__(self, screen, cov_settings, window, x_pos=None, y_pos=None):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.cov_settings = cov_settings
        self.side_window_rect = window.rect_2
        self.image = cov_settings.human_img
        self.rect = self.image.get_rect()
        if not (x_pos and y_pos):
            self.rect.centerx = randint(self.side_window_rect.left + self.rect.width,
                                        self.side_window_rect.right - self.rect.width)
            self.rect.centery = randint(self.side_window_rect.top + self.rect.width,
                                        self.side_window_rect.bottom - self.rect.width)
        elif x_pos or y_pos:
            self.rect.centerx = x_pos
            self.rect.centery = y_pos
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)
        self.direct_x = 0
        self.direct_y = 0
        self.steps = 0

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.steps <= 0:
            self.direct_x = randint(-self.cov_settings.human_speed, self.cov_settings.human_speed) / 100
            self.direct_y = randint(-self.cov_settings.human_speed, self.cov_settings.human_speed) / 100
            self.steps = randint(1, self.cov_settings.max_steps)
        elif self.steps > 0:
            if self.rect.right >= self.side_window_rect.right:
                self.direct_x *= -1
                self.center_x -= 4
            elif self.rect.left <= self.side_window_rect.left:
                self.direct_x *= -1
                self.center_x += 4
            if self.rect.bottom >= self.side_window_rect.bottom:
                self.direct_y *= -1
                self.center_y -= 4
            elif self.rect.top <= self.side_window_rect.top:
                self.direct_y *= -1
                self.center_y += 4
            self.center_x += self.direct_x
            self.center_y += self.direct_y
            self.steps -= 1
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def change_skin(self, image):
        last_centerx = self.rect.centerx
        last_centery = self.rect.centery
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = last_centerx
        self.rect.centery = last_centery