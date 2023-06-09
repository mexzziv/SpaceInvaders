import pygame, sys
from player import Player
import obstacle

class Game:
    def __init__(self):
        # Player setup
        player_sprite = Player((scree_width / 2, screen_height), scree_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Obstacle setup
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.create_obstacle(40,480)

    def create_obstacle(self, x_start, y_start):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = x_start + col_index * self.block_size
                    y = y_start + row_index * self.block_size
                    block = obstacle.Block(self.block_size, (241, 79, 80), x, y)
                    self.blocks.add(block)

    def run(self):
        self.player.update()

        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)

        self.blocks.draw(screen)
        # update all sprites groups
        # draw all sprite groups

if __name__ == '__main__':
    pygame.init()
    scree_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((scree_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill((30, 30, 30))
        game.run()

        pygame.display.flip()
        clock.tick(60)