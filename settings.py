import pygame


class Settings:
    def __init__(self):
        """Screen_set"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_image = pygame.image.load('images/covid-19_2.png')
        """Window_set"""
        self.frame_size = 5
        self.window_width_1 = self.screen_width // 2
        self.window_height_1 = self.screen_height - self.frame_size * 2 - 10
        self.window_width_2 = self.window_width_1 - self.frame_size * 2
        self.window_height_2 = self.screen_height - self.frame_size * 4 - 10
        self.window_color_1 = 166, 46, 46
        self.window_color_2 = 43, 43, 43
        self.area = 0.018172
        """Human_set"""
        self.infctd_human_img = pygame.image.load('images/infctd_human_2.png')
        self.human_img = pygame.image.load('images/human_2.png')
        self.img_wsd_hands = pygame.image.load('images/human_wshd_hands.png')
        self.dead_img = pygame.image.load('images/dead.png')
        self.pct_wsd_hands = 0
        self.population = 5000
        self.max_steps = 40
        self.human_speed = 100
        self.mortality = 1
        """Buttons"""
        self.restart_bttn_img = pygame.image.load('images/Button_restart_1.png')
        self.restart_bttn_x_pos = 666
        self.restart_bttn_y_pos = 330
        self.statistics_bttn_img = pygame.image.load('images/statistics_button.png')
        self.statistics_bttn_x_pos = 666
        self.statistics_bttn_y_pos = 385
        self.plus_bttn_img = pygame.image.load('images/Button_+.png')
        self.plus_bttn_x_pos = 659
        self.plus_bttn_y_pos = 330
        self.minus_bttn_img = pygame.image.load('images/Button_-.png')
        self.minus_bttn_x_pos = 712
        self.minus_bttn_y_pos = 330
        self.infctd_cursor_bttn_img = pygame.image.load('images/Infctd_cursor_button.png')
        self.infctd_cursor_bttn_x_pos = 1070
        self.infctd_cursor_bttn_y_pos = 330
        """Sliders"""
        self.slider_1_dot_x_pos = 652
        self.slider_1_dot_y_pos = 187
        self.slider_2_dot_x_pos = 1093
        self.slider_2_dot_y_pos = 271
        self.slider_3_dot_x_pos = 652
        self.slider_3_dot_y_pos = 367
