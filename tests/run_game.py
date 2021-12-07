import pygame
from snake_gym.game import World, Snake


clock = pygame.time.Clock()


def main():

    # create snake
    snake = Snake()

    # create world
    world = World(snake)

    # draw environment
    world.draw()

    # set initial direction
    direction = "RIGHT"
    xy_move = [1, 0]

    done = False
    i = 0
    while not done:
        df = clock.tick(8)

        # check all events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            ########################
            # check for user input #
            ########################

            if event.type == pygame.KEYDOWN:
                # check if direction is not opposing for all moves, then set it
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"

                    # save x and y changes in coordinates
                    xy_move = [-1, 0]

                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

                    # save x and y changes in coordinates
                    xy_move = [1, 0]

                elif event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"

                    # save x and y changes in coordinates
                    xy_move = [0, -1]

                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"

                    # save x and y changes in coordinates
                    xy_move = [0, 1]

        # update snake
        snake.move(xy_move)

        # draw new board state
        world.draw()


if __name__ == "__main__":
    main()
