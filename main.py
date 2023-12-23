import math
import pygame

black = (0, 0, 0)
white = (255, 255, 255)


class Pendulum:
    def __init__(self, pivot_x, pivot_y, m, a, g, color, l):
        self.pivot = (pivot_x, pivot_y)
        self.m = m
        self.l = l
        self.a = a
        self.g = g
        self.color = color

        self.x = 0
        self.y = 0

        self.av = 0
        self.trajectory = []

    def step(self):
        acc = (-self.g / self.l) * math.sin(self.a)
        self.av += acc
        self.av *= 5

        self.a += self.av
        self.x = self.pivot[0] + self.l * math.sin(self.a)
        self.y = self.pivot[1] + self.l * math.cos(self.a)



    def draw(self, surface):
        pygame.draw.line(surface, white, self.pivot, (self.x, self.y))
        pygame.draw.circle(surface, self.color, (self.x, self.y), 15)


def init_surface(size, caption):
    pygame.init()
    pygame.display.set_caption(caption)
    surface = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    return surface, clock


def run():
    width, height = 800, 800

    fps = 60

    surface, clock = init_surface((width, height), "Simple Game")

    lengths = [200+30 * i for i in range(7)]

    colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'grey']

    pend_list = [Pendulum(pivot_x=width//2, pivot_y=height//2, m=1, a=math.pi/2, g=1, color=c, l=l) for l, c in zip(lengths, colors )]

    stop = False

    while not stop:
        clock.tick(fps)
        surface.fill(black)

        for pendulum in pend_list:
            for event in pygame.event.get():
                stop = event.type == pygame.QUIT
            pendulum.step()
            pendulum.draw(surface)

        pygame.display.flip()
    pygame.quit()

run()
