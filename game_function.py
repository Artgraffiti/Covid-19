import sys
import pygame
from human import Human
from random import randint
import matplotlib.pyplot as plt


def check_events(population, wsd_hands_population, infctd_population, screen, cov_settings, window, USEREVENT, timeline,
                 infctd_inf, button_restart, button_infctd_cursor, button_statistics, sliders_list,
                 infctd_cursor):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            create_statistic(infctd_inf, timeline)
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, population, wsd_hands_population, infctd_population,
                                 screen, cov_settings, window, infctd_inf, timeline)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, population, cov_settings)
        elif event.type == USEREVENT + 1:
            human_infecting(population, infctd_population, wsd_hands_population, cov_settings)
            create_list_covid19(infctd_population, timeline, infctd_inf)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_infctd_cursor(screen, window, infctd_population, infctd_cursor, cov_settings, mouse_x, mouse_y)
            check_button_infctd_cursor(button_infctd_cursor, mouse_x, mouse_y, infctd_cursor)
            check_button_restart(button_restart, mouse_x, mouse_y, screen, window,
                                 cov_settings, infctd_population, wsd_hands_population, population)
            check_button_statistics(button_statistics, infctd_inf, timeline, mouse_x, mouse_y)
            for slider in sliders_list:
                check_slider(slider, mouse_x, mouse_y)
        elif event.type == pygame.MOUSEBUTTONUP:
            for slider in sliders_list:
                slider.updating = False


def check_keydown_events(event, population, wsd_hands_population, infctd_population,
                         screen, cov_settings, window, infctd_inf, timeline):
    if event.key == pygame.K_q:
        create_statistic(infctd_inf, timeline)
        sys.exit()
    elif event.key == pygame.K_1:
        for human in population:
            human.change_skin(cov_settings.infctd_human_img)
    elif event.key == pygame.K_2:
        create_infctd_human(screen, cov_settings, window, infctd_population)
    elif event.key == pygame.K_r:
        reset_infection(screen, window, cov_settings, infctd_population, wsd_hands_population, population)


def check_keyup_events(event, population, cov_settings):
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_1:
        for human in population:
            human.change_skin(cov_settings.human_img)


def update_sprites(screen, window, population, wsd_hands_population, infctd_population, infctd_cursor, slider_1,
                   slider_2, cov_settings):
    population.update()
    wsd_hands_population.update()
    infctd_population.update()
    if infctd_cursor.active:
        infctd_cursor.update()
        check_infctd_cursor_collisions(infctd_cursor, population)
    elif slider_1.updating:
        cov_settings.population = slider_1.update() // cov_settings.area
        reset_infection(screen, window, cov_settings, infctd_population, wsd_hands_population, population)
    elif slider_2.updating:
        cov_settings.population = slider_2.update()
        reset_infection(screen, window, cov_settings, infctd_population, wsd_hands_population, population)


def update_screen(screen, window, population, wsd_hands_population, infctd_population, bg_image, infctd_cursor,
                  buttons_list, sliders_list):
    bg_image.show()
    window.draw_window()
    population.draw(screen)
    wsd_hands_population.draw(screen)
    infctd_population.draw(screen)
    draw_layouts(buttons_list)
    draw_layouts(sliders_list)
    if infctd_cursor.active:
        infctd_cursor.draw()
    pygame.display.flip()


def create_infctd_human(screen, cov_settings, window, infctd_population, x_pos=None, y_pos=None):
    infctd_human = Human(screen, cov_settings, window, x_pos, y_pos)
    infctd_human.change_skin(cov_settings.infctd_human_img)
    infctd_population.add(infctd_human)


def create_population(screen, cov_settings, window, population):
    for i in range(int(cov_settings.population * (1 - cov_settings.pct_wsd_hands))):
        human = Human(screen, cov_settings, window)
        human.rect.centerx = randint(human.side_window_rect.left + human.rect.width // 2,
                                     human.side_window_rect.right - human.rect.width // 2)
        human.rect.centery = randint(human.side_window_rect.top + human.rect.width // 2,
                                     human.side_window_rect.bottom - human.rect.width // 2)
        population.add(human)


"""don't working"""


def granulate_infctd_population(infctd_population, new_group):
    if len(infctd_population) >= 70:
        infctd_population_g = pygame.sprite.Group()
        infctd_population_sprites = infctd_population.sprites()
        while len(infctd_population_sprites) > 70:
            deleted_infctd_human = infctd_population_sprites.pop()
            infctd_population.remove(deleted_infctd_human)
            infctd_population_g.add(deleted_infctd_human)
        new_group.add(infctd_population_g)


"""don't working"""


def create_wsd_hands_population(screen, window, cov_settings, wsd_hands_population):
    for i in range(int(cov_settings.population * cov_settings.pct_wsd_hands)):
        wsd_hands_human = Human(screen, cov_settings, window)
        wsd_hands_human.rect.centerx = randint(wsd_hands_human.side_window_rect.left + wsd_hands_human.rect.width // 2,
                                               wsd_hands_human.side_window_rect.right - wsd_hands_human.rect.width // 2)
        wsd_hands_human.rect.centery = randint(wsd_hands_human.side_window_rect.top + wsd_hands_human.rect.width // 2,
                                               wsd_hands_human.side_window_rect.bottom - wsd_hands_human.rect.width // 2)
        wsd_hands_human.change_skin(cov_settings.img_wsd_hands)
        wsd_hands_population.add(wsd_hands_human)


def reset_infection(screen, window, cov_settings, infctd_population, wsd_hands_population, population):
    infctd_population.empty()
    population.empty()
    wsd_hands_population.empty()
    create_population(screen, cov_settings, window, population)
    create_wsd_hands_population(screen, window, cov_settings, wsd_hands_population)


def human_infecting(population, infctd_population, wsd_hands_population, cov_settings):
    collisions_1 = pygame.sprite.groupcollide(infctd_population, population, False, False)
    if collisions_1:
        for infctd_humans in collisions_1.values():
            for infctd_human in infctd_humans:
                infctd_human.change_skin(cov_settings.infctd_human_img)
                population.remove(infctd_human)
                infctd_population.add(infctd_human)
    collisions_2 = pygame.sprite.groupcollide(infctd_population, wsd_hands_population, False, False)
    if collisions_2:
        random = randint(3, 10)
        if random <= 3:
            for infctd_humans in collisions_2.values():
                for infctd_human in infctd_humans:
                    infctd_human.change_skin(cov_settings.infctd_human_img)
                    population.remove(infctd_human)
                    infctd_population.add(infctd_human)


def create_list_covid19(infctd_population, timeline, infctd_inf):
    timeline.append(pygame.time.get_ticks() // 1000)
    infctd_inf.append(len(infctd_population))


def create_statistic(infctd_inf, timeline):
    plt.plot(timeline, infctd_inf, linewidth=5)
    plt.title("Кол-во зараженных COVID-19", fontsize=24)
    plt.xlabel("Время(сек)", fontsize=12)
    plt.ylabel("Зараженные", fontsize=12)
    plt.tick_params(axis='both', labelsize=10)
    plt.show()


def check_infctd_cursor(screen, window, infctd_population, infctd_cursor, cov_settings, mouse_x, mouse_y):
    if infctd_cursor.active and window.rect_2.collidepoint(mouse_x, mouse_y):
        create_infctd_human(screen, cov_settings, window, infctd_population, mouse_x, mouse_y)


def check_infctd_cursor_collisions(infctd_cursor, population):
    collisions = pygame.sprite.spritecollide(infctd_cursor, population, False, pygame.sprite.collide_circle)
    if collisions:
        for human in collisions:
            if human.rect.centerx > infctd_cursor.rect.centerx:
                human.direct_x *= -1
                human.center_x += 2
            elif human.rect.centerx < infctd_cursor.rect.centerx:
                human.direct_x *= -1
                human.center_x -= 2
            if human.rect.centery > infctd_cursor.rect.centery:
                human.direct_y *= -1
                human.center_y += 2
            elif human.rect.centerx < infctd_cursor.rect.centerx:
                human.direct_y *= -1
                human.center_y -= 2


def draw_layouts(layout_list):
    for layout in layout_list:
        layout.draw()


"""Buttons"""


def check_button_restart(button_restart, mouse_x, mouse_y, screen, window,
                         cov_settings, infctd_population, wsd_hands_population, population):
    if button_restart.rect.collidepoint(mouse_x, mouse_y):
        reset_infection(screen, window, cov_settings, infctd_population, wsd_hands_population, population)


def check_button_infctd_cursor(button_infctd_cursor, mouse_x, mouse_y, infctd_cursor):
    if button_infctd_cursor.rect.collidepoint(mouse_x, mouse_y):
        infctd_cursor.cursor_visible = not infctd_cursor.cursor_visible
        pygame.mouse.set_visible(infctd_cursor.cursor_visible)
        infctd_cursor.active = not infctd_cursor.active


def check_button_statistics(button_statistics, infctd_inf, timeline, mouse_x, mouse_y):
    if button_statistics.rect.collidepoint(mouse_x, mouse_y):
        create_statistic(infctd_inf, timeline)


"""Sliders"""


def check_slider(slider, mouse_x, mouse_y):
    if slider.dot_rect.collidepoint(mouse_x, mouse_y) or slider.line_rect.collidepoint(mouse_x, mouse_y):
        slider.updating = True


def dead(infctd_population, cov_settings, the_dead):
    for human in infctd_population:
        random = randint(1, 100)
        if random <= cov_settings.mortality:
            human.change_skin(cov_settings.dead_img)
            infctd_population.remove(human)
            the_dead.add(human)
