class Room():
    def __init__(self, description="", north=0, east=0, west=0, south=0):
        self.description = description
        self.north = north
        self.east = east
        self.west = west
        self.south = south


def main():

    room_list = []
    room = Room("You are in a dusty castle room. \nPassages lead to the north and south.", None, 1, 3, 2)
    room_list.append(room)

    current_room = 0

    done = False

    while done is False:

        current_room = 0
        print("")
        print(room_list[0].description)

        user_Choice = input("What direction?  ")

        if user_Choice.upper() == "N":

            next_room = room_list[current_room].north

           # print(next_room) debug

            if next_room is None:
                print(" You are in the north hall. You can’t go that way.")
            else:
                current_room = next_room

        elif user_Choice.upper() == "E":

            next_room = room_list[current_room].east
           # print(next_room) debug

            if next_room is None:
                print("You can’t go that way.")
            else:
                current_room = next_room
                print("“You are in the master bedroom . There is a door to the north.”")

        elif user_Choice.upper() == "W":

            next_room = room_list[current_room].west
            #print(next_room)  # debug

            if next_room is None:
                print("You can’t go that way.")
            else:
                current_room = next_room
                print("“You are in the kitchen. There is a door to South.”")

        elif user_Choice.upper() == "S":

            next_room = room_list[current_room].south
           # print(next_room)  # debug

            if next_room is None:
                print("You can’t go that way.")
            else:
                current_room = next_room
                print("“You are in the a bedroom. There is a door to west.”")

        elif user_Choice.upper() == "Q":
            print("")
            print("You have quiet the game")
            done = True

        else:
            print("Please type a valid character such as n(for north), \ne(for east), w(for west) and s(for south) or q to quiet")


main()


