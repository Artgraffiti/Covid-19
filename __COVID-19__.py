import pygame
from settings import Settings
import game_function as gf
from window import Window
from button import Button
from slider import Slider
from infctd_cursor import Infctd_Cursor
from pygame.sprite import Group
from bg_image import BG_Image
from pygame.locals import *

FPS = 30


def run_game():
    pygame.init()
    clock = pygame.time.Clock()
    cov_settings = Settings()
    screen = pygame.display.set_mode((cov_settings.screen_width, cov_settings.screen_height))
    pygame.display.set_caption('COVID-19')
    window = Window(screen, cov_settings)
    bg_image = BG_Image(screen, cov_settings)

    """Buttons"""
    button_restart = Button(screen, cov_settings.restart_bttn_img,
                            cov_settings.restart_bttn_x_pos, cov_settings.restart_bttn_y_pos)
    button_statistics = Button(screen, cov_settings.statistics_bttn_img,
                               cov_settings.statistics_bttn_x_pos, cov_settings.statistics_bttn_y_pos)
    button_infctd_cursor = Button(screen, cov_settings.infctd_cursor_bttn_img,
                                  cov_settings.infctd_cursor_bttn_x_pos, cov_settings.infctd_cursor_bttn_y_pos)
    buttons_list = [button_restart, button_infctd_cursor, button_statistics]

    """Sliders"""
    slider_1 = Slider(screen, cov_settings.slider_1_dot_x_pos, cov_settings.slider_1_dot_y_pos, 10, 1, 110)
    slider_2 = Slider(screen, cov_settings.slider_2_dot_x_pos, cov_settings.slider_2_dot_y_pos, 50, 1, 6000)
    sliders_list = [slider_1, slider_2]

    infctd_cursor = Infctd_Cursor(screen)
    population, wsd_hands_population, infctd_population, the_dead = Group(), Group(), Group(), Group()
    timeline, infctd_inf = [], []
    gf.create_population(screen, cov_settings, window, population)
    gf.create_wsd_hands_population(screen, window, cov_settings, wsd_hands_population)
    pygame.time.set_timer(USEREVENT + 1, 3000)
    while True:
        clock.tick(FPS)
        gf.check_events(population, wsd_hands_population, infctd_population, screen, cov_settings, window, USEREVENT,
                        timeline, infctd_inf, button_restart, button_infctd_cursor, button_statistics, sliders_list,
                        infctd_cursor)
        gf.update_sprites(screen, window, population, wsd_hands_population, infctd_population, infctd_cursor, slider_1,
                          slider_2, cov_settings)
        gf.update_screen(screen, window, population, wsd_hands_population, infctd_population, bg_image, infctd_cursor,
                         buttons_list, sliders_list)


run_game()
