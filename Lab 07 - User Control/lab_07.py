""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class Ball:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.background = arcade.load_texture("3739446.png")

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.RED)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(300, 300, SCREEN_WIDTH,
                                      SCREEN_HEIGHT, self.background)
        self.ball.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        laser_sound = arcade.load_sound("laser.wav")
        arcade.play_sound(laser_sound)


    def on_mouse_motion(self, x, y, dx, dy):
            """ Called to update our objects.
            Happens approximately 60 times per second."""
            self.ball.position_x = x
            self.ball.position_y = y


def main():
    window = MyGame()
    arcade.run()


main()