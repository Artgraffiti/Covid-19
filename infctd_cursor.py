import pygame


class Infctd_Cursor:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/infctd_cursor_circle.png')
        self.rect = self.image.get_rect()
        self.radius = self.rect.height // 2
        self.rect.centerx = -20
        self.rect.centery = -20
        self.cursor_visible = True
        self.active = False

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.rect.centerx = mouse_x
        self.rect.centery = mouse_y

    def draw(self):
        self.screen.blit(self.image, self.rect)