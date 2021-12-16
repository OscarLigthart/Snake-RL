import pygame
from pygame.locals import *
from snake_gym import Env
from snake_gym.game.actions import Actions


clock = pygame.time.Clock()


def main():
    """
    Main function to play the game
    """

    # initialize event
    env = Env(human_player=True)

    # start by going right
    action = Actions.RIGHT

    done = False
    while not done:

        df = clock.tick(10)

        # check all events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            ########################
            # check for user input #
            ########################

            if event.type == pygame.KEYDOWN:

                # set the appropriate action for the appropriate key
                if event.key == pygame.K_LEFT:
                    action = Actions.LEFT

                elif event.key == pygame.K_RIGHT:
                    action = Actions.RIGHT

                elif event.key == pygame.K_UP:
                    action = Actions.UP

                elif event.key == pygame.K_DOWN:
                    action = Actions.DOWN

        # need to take a step here, keep track of
        state, reward, done = env.step(action)


if __name__ == "__main__":
    main()
