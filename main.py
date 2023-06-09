import pygame, sys
from player import Player

class Game:
    def __init__(self):
        player_sprite = Player((scree_width / 2, screen_height), scree_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.update()

        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
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