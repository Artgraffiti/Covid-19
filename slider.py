import pygame


class Slider:
    def __init__(self, screen, x_pos, y_pos, default_value, min_value, max_value):
        self.screen = screen
        self.value = default_value
        self.min = min_value
        self.max = max_value - self.min
        self.dot_img = pygame.image.load('images/slider_dot.png')
        self.dot_rect = self.dot_img.get_rect()
        self.dot_rect.x = x_pos
        self.dot_rect.centery = y_pos + self.dot_rect.height // 2
        self.line_img_example = pygame.image.load('images/slider_line.png')
        self.line_img = pygame.image.load('images/slider_line.png')
        self.line_rect = self.line_img.get_rect()
        self.line_rect.x = 666
        self.line_rect.centery = self.dot_rect.centery
        self.line_img = pygame.transform.scale(self.line_img_example,
                                               (self.dot_rect.centerx - self.line_rect.left, self.line_rect.height))
        self.updating = False

    def draw(self):
        self.screen.blit(self.line_img, self.line_rect)
        self.screen.blit(self.dot_img, self.dot_rect)

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.updating and self.line_rect.left <= mouse_x <= self.line_rect.right:
            self.dot_rect.centerx = mouse_x
            self.line_img = pygame.transform.scale(self.line_img_example,
                                                   (self.dot_rect.centerx - self.line_rect.left,
                                                    self.line_rect.height))
            self.value = int(self.min + self.max * round((self.dot_rect.centerx - self.line_rect.left)
                                                         / (self.line_rect.width - 1), 2))
        return self.value
