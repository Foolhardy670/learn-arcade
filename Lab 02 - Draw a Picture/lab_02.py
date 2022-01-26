import arcade

if __name__ == '__main__':
    arcade.open_window(800, 750, 'Draw a picture')
    arcade.set_background_color(arcade.color.CADET) # setting the background color to blue
    arcade.start_render()
    # Draw a sun
    arcade.draw_circle_filled(80, 680, 60, arcade.color.CADMIUM_YELLOW, 2)
    # draw a house
    arcade.draw_rectangle_filled(400, 270, 500, 600, arcade.color.BRILLIANT_LAVENDER, 90)
    arcade.draw_rectangle_filled(400, 85, 130, 90, arcade.color.BRIGHT_UBE, 90)
    arcade.draw_point(415, 95, arcade.color.RED, 10)
    arcade.draw_rectangle_outline(195, 400, 100, 100,
                                  arcade.color.BRIGHT_CERULEAN, 3)
    # House Windows
    arcade.draw_rectangle_outline(195, 150, 100, 100,
                                  arcade.color.BRIGHT_CERULEAN, 3)
    # House Windows
    arcade.draw_rectangle_outline(250, 400, 100, 100,
                                  arcade.color.BRIGHT_CERULEAN, 3)
    # House Windows
    arcade.draw_rectangle_outline(250, 150, 100, 100,
                                  arcade.color.BRIGHT_CERULEAN, 3)
    # House Windows

    arcade.draw_rectangle_outline(595, 400, 100, 100,
                                  arcade.color.BRIGHT_CERULEAN, 3)
    # House Windows
    arcade.draw_rectangle_outline(595, 150, 100, 100,
                                  arcade.color.BRIGHT_CERULEAN, 3)
    # House Windows
    arcade.draw_rectangle_outline(550, 400, 100, 100,
                                  arcade.color.BRIGHT_CERULEAN, 3)
    # House Windows
    arcade.draw_rectangle_outline(550, 150, 100, 100,
                                  arcade.color.BRIGHT_CERULEAN, 3)
    # draw house roof
    arcade.draw_triangle_filled(400, 700,
                                700, 520,
                                100, 520,
                                arcade.color.BONE)
    #  Draw house roof Window
    arcade.draw_circle_outline(400, 600, 50, arcade.color.BRIGHT_CERULEAN, 3)
    arcade.draw_line(400, 650, 400, 550, arcade.color.WOOD_BROWN, 3)

    arcade.finish_render()
    arcade.run()



