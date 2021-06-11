import random
from game import constants
from game.action import Action
from game.point import Point


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        paddle = cast["paddle"][0] # there's only one
        bricks = cast["brick"]
        ball = cast["ball"][0]
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                #delete the brick
                cast["brick"].remove(brick)
                ball.set_y_velocity(ball.get_velocity().get_y() * -1)

        b_pos = ball.get_position()
        if b_pos.get_y() == 1:# or b_pos.get_y() == constants.MAX_Y -1:
            ball.set_y_velocity(ball.get_velocity().get_y() * -1)
        #if b_pos.get_x() == 1 or b_pos.get_x() == constants.MAX_X -1:
        #    ball.set_x_velocity(ball.get_velocity().get_x() * -1)

        p_pos = paddle.get_position()
        if (b_pos.get_y() == p_pos.get_y() - 1) and (b_pos.get_x() >= p_pos.get_x() and b_pos.get_x() < p_pos.get_x() + 12):
            ball.set_y_velocity(ball.get_velocity().get_y() * -1)