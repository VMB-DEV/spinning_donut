import pygame
from spinning_donut import SpinningDonut

class Animation:
    def __init__(self, windowSize, background_color = (25, 25, 25)):
        self._screen = pygame.display.set_mode((windowSize, windowSize))
        self._backgroundColor = background_color
        self._windowSize = windowSize
        self._clock = pygame.time.Clock()
        self._fps = 60
        self._donut = SpinningDonut(self._windowSize)

    def engine(self):
        pygame.init()
        self._screen = pygame.display.set_mode((self._windowSize, self._windowSize))
        self._clock = pygame.time.Clock()
        running = True
        while running:
            self._screen.fill((self._backgroundColor))
            self._clock.tick(self._fps)
            self._donut.update_donut_position()
            self._donut.draw_donut(self._screen)
            pygame.display.update()
