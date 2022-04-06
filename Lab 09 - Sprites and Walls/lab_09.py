

import arcade
import random
import os

SPRITE_SCALING = 0.5
SPRITE_SCALING_COIN = 0.2

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Sprite No Coins on Walls Example"

NUMBER_OF_COINS = 50

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.all_sprites_list = None
        self.coin_list = None

        # Set up the player
        self.player_sprite = None
        self.wall_list = None
        self.physics_engine = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        self.player_sprite = arcade.Sprite("character1.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64

        # -- Set up the walls
        # Create a series of horizontal walls
        # -- Set up the walls
        # Create a row of boxes
        for x in range(73, 1190, 64):
            wall = arcade.Sprite("tile_0021.v3.png",
                                 SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 10
            self.wall_list.append(wall)

        for x in range(373, 1090, 140):
            wall = arcade.Sprite("tile_0014.v3.png",
                                 SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 240
            self.wall_list.append(wall)

        for x in range(273, 1190, 67):
            wall = arcade.Sprite("tile_0014.v3.png",
                                 SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 620
            self.wall_list.append(wall)

        for x in range(173, 490, 64):
            wall = arcade.Sprite("tile_0014.v3.png",
                                 SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 140
            self.wall_list.append(wall)

        for x in range(173, 790, 130):
            wall = arcade.Sprite("tile_0014.v3.png",
                                 SPRITE_SCALING)
            wall.center_x = x + 400
            wall.center_y = 140
            self.wall_list.append(wall)

        for x in range(173, 1090, 204):
            wall = arcade.Sprite("tile_0014.v3.png",
                                 SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 370
            self.wall_list.append(wall)

        for x in range(173, 490, 64):
            wall = arcade.Sprite("tile_0014.v3.png",
                                 SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 490
            self.wall_list.append(wall)

        for x in range(600, 1090, 64):
            wall = arcade.Sprite("tile_0014.v3.png",
                                 SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 490
            self.wall_list.append(wall)

        for x in range(73, 1190, 64):
            wall = arcade.Sprite("tile_0021.v3.png",
                                 SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 700
            self.wall_list.append(wall)

        # Create a column of boxes
        for y in range(73, 800, 64):
            wall = arcade.Sprite("tile_0021.v3.png",
                                 SPRITE_SCALING)
            wall.center_x = 10
            wall.center_y = y - 40
            self.wall_list.append(wall)

        for y in range(73, 800, 64):
            wall = arcade.Sprite("tile_0021.v3.png",
                                 SPRITE_SCALING)
            wall.center_x = 1200
            wall.center_y = y - 40
            self.wall_list.append(wall)

        # -- Randomly place coins where there are no walls
        # Create the coins
        for i in range(NUMBER_OF_COINS):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)



            # --- IMPORTANT PART ---



            # Boolean variable if we successfully placed the coin

            coin_placed_successfully = False



            # Keep trying until success

            while not coin_placed_successfully:

                # Position the coin

                coin.center_x = random.randrange(SCREEN_WIDTH)

                coin.center_y = random.randrange(SCREEN_HEIGHT)



                # See if the coin is hitting a wall

                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)



                # See if the coin is hitting another coin

                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)



                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:

                    # It is!

                    coin_placed_successfully = True



            # Add the coin to the lists

            self.coin_list.append(coin)



            # --- END OF IMPORTANT PART ---

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.ANTIQUE_FUCHSIA)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        # Draw all the sprites.
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_sprite.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(text=output, start_x=10, start_y=20,
                         color=arcade.color.WHITE, font_size=14)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            laser_sound = arcade.load_sound("laser.wav")
            arcade.play_sound(laser_sound)
            coin.remove_from_sprite_lists()
            self.score += 1

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()