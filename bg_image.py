class BG_Image:
    def __init__(self, screen, cov_settings):
        self.screen = screen
        self.image = cov_settings.bg_image
        self.rect = self.screen.get_rect()

    def show(self):
        self.screen.blit(self.image, self.rect)
