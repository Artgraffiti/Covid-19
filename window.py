import pygame


class Window:
    def __init__(self, screen, cov_settings):
        self.screen = screen
        self.rect_1 = pygame.Rect(10, 10, cov_settings.window_width_1, cov_settings.window_height_1)
        self.rect_2 = pygame.Rect(10 + cov_settings.frame_size, 10 + cov_settings.frame_size,
                                  cov_settings.window_width_2, cov_settings.window_height_2)
        self.window_color_1 = cov_settings.window_color_1
        self.window_color_2 = cov_settings.window_color_2

    def draw_window(self):
        pygame.draw.rect(self.screen, self.window_color_1, self.rect_1)
        pygame.draw.rect(self.screen, self.window_color_2, self.rect_2)
