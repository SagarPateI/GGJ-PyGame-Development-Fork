import pygame as pg
import sys
from GameLib.level1 import Level1
from GameLib.test import Test
from GameLib.Menu.Button import Button


class Menu:
    def __init__(self, dims, enable_test_level=True):
        pg.init()
        self.width, self.height = dims
        self.screen = pg.display.set_mode(dims)
        pg.display.set_caption("Main Menu")
        self.clock = pg.time.Clock()
        self.fps = 60

        # Menu settings
        self.font = pg.font.SysFont("Consolas", 25)
        self.enable_test_level = enable_test_level

        # Buttons
        self.start_button = Button(150, 400, 150, 50)
        self.settings_button = Button(350, 400, 150, 50)
        self.quit_button = Button(550, 400, 150, 50)
        self.test_button = Button(350, 200, 150, 50)

    def handle_input(self):
        mx, my = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1 and self.quit_button.isClicked((mx, my)):
                    pg.quit()
                    sys.exit()

                if event.button == 1 and self.start_button.isClicked((mx, my)):
                    Level1((800, 600)).run()

                if (
                    event.button == 1
                    and self.enable_test_level
                    and self.test_button.isClicked((mx, my))
                ):
                    Test((800, 600)).run()

    def draw_menu(self):
        self.screen.fill((0, 0, 0))

        self.start_button.draw(self.screen)
        self.settings_button.draw(self.screen)
        self.quit_button.draw(self.screen)
        if self.enable_test_level:
            self.test_button.draw(self.screen)

        self.draw_text(
            "Bubble Blast Deluxe Unlimited Edition ft. Glasscord Team",
            self.font,
            (255, 255, 255),
            self.screen,
            int(self.width / 2) - 393,
            20,
        )
        self.draw_text("Start Game", self.font, (255, 255, 255), self.screen, 155, 415)
        self.draw_text("Settings", self.font, (255, 255, 255), self.screen, 375, 415)
        if self.enable_test_level:
            self.draw_text("Test", self.font, (255, 255, 255), self.screen, 395, 215)
        self.draw_text("Quit", self.font, (255, 255, 255), self.screen, 595, 415)

        pg.display.flip()

    def draw_text(self, text, font, color, surface, x, y):
        text_obj = font.render(text, 1, color)
        text_rect = text_obj.get_rect()
        text_rect.topleft = (x, y)
        surface.blit(text_obj, text_rect)

    def run(self):
        while True:
            self.handle_input()
            self.draw_menu()
            self.clock.tick(self.fps)
