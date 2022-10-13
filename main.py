import pygame
from pygame.math import Vector2
import sys
from random import choice


class Application:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True

        self.triangle = [Vector2(200, 400), Vector2(400, 100), Vector2(600, 400)]
        self.pivot = Vector2(300, 300)
        self.new_points = []
        self.new_points.append(self.pivot)

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    pygame.quit()
                    sys.exit()

    def update(self):

        new_point = (choice(self.triangle) - self.pivot) // 2 + self.pivot
        self.new_points.append(new_point)
        self.pivot = new_point
        print(len(self.new_points))
        if len(self.new_points) >= 2000:
            self.new_points.pop(0)

    def draw(self):
        self.screen.fill((0, 0, 0))

        # start setup
        pygame.draw.rect(self.screen, (255, 255, 255), (self.triangle[0], (1, 1)), 1)
        pygame.draw.rect(self.screen, (255, 255, 255), (self.triangle[1], (1, 1)), 1)
        pygame.draw.rect(self.screen, (255, 255, 255), (self.triangle[2], (1, 1)), 1)


        for point in self.new_points:
            pygame.draw.rect(self.screen, (255, 255, 255), (point, (1, 1)), 1)

        pygame.display.flip()


if __name__ == '__main__':
    app = Application()
    app.run()