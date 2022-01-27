import arcade

"""
Open new window for Draw Using Fucntions
Use Lab 2 house draw and put into a function
"""

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 750

""" ADD more design by drawing trees and the sun and drones"""

def draw_drone(x, y):
    # draw a bird
    arcade.draw_arc_outline(x, y, 50, 50, arcade.color.BLACK, 5, 90)
    arcade.draw_arc_outline(x + 20, y, 50, 50, arcade.color.BLACK, 90, 180)

# draw the sun
def draw_sun(x, y):
    arcade.draw_circle_filled(x, y, 60, arcade.color.CADMIUM_YELLOW, 2)


def draw_tree(x, y):
    """
    This function draws a  tree at a specified location.
    """
    # Draw the triangle on top of the trunk
    arcade.draw_triangle_filled(x + 40, y,
                                x, y - 100,
                                x + 80, y - 100,
                                arcade.color.DARK_GREEN)

    # Draw the trunk
    arcade.draw_lrtb_rectangle_filled(x + 30, x + 50, y - 100, y - 160,
                                      arcade.color.DARK_BROWN)

# Function draw the house

def draw_house():
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
    arcade.draw_line(400, 650, 400, 550, arcade.color.WOOD_BROWN, 3)  # draw line


# draw main picture
def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
    arcade.start_render()

    # Draw the ground
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AMAZON)

    # Call our drawing functions.
    draw_house()
    draw_sun(80, 680)
    draw_tree(750, 320)
    draw_tree(850, 220)
    draw_tree(950, 120)
    draw_tree(1050, 320)
    draw_tree(1150, 220)
    draw_tree(1250, 320)
    draw_drone(1300, 600)
    draw_drone(1270, 350)
    draw_drone(1100, 400)
    draw_drone(970, 350)
    draw_drone(1050, 560)




    # Finish and run
    arcade.finish_render()
    arcade.run()

main()