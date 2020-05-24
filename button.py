class Button:
    def __init__(self, screen, img, x_pos, y_pos):
        self.screen = screen
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def draw(self):
        self.screen.blit(self.image, self.rect)
