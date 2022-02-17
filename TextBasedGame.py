# Arica N. Bryant

# function that shows the objective of the game along with commands
def instructions():
    print('Welcome to the Alien Escape Text Adventure Game!')
    print('The goal is to collect all 6 items scattered around the spaceship')
    print('Find the Alien Commander before collecting all the items and its game over!')
    print('Movement commands: North, South, East, West')
    print('Add an item to Inventory: get "item name"\n')


# function to show current status
def status(cur_room, cur_inventory, room_item):
    print('You are currently in the', cur_room)
    print('Inventory: ', cur_inventory)
    print('* ' * 10)  # print out a design
    if room_item == 'empty':
        print('The room is empty')
    else:
        print('There is a', room_item, 'in the room')


def main():
    # dictionary linking rooms together
    rooms = {
        'Prison Cells': {'South': 'Laboratory', 'East': 'Defense Repository'},
        'Laboratory': {'North': 'Prison Cells', 'item': 'Healing Potion'},
        'Defense Repository': {'West': 'Prison Cells', 'North': 'Guards Chamber', 'East': 'Knowledge Center',
                               'item': 'Blaster'},
        'Knowledge Center': {'West': 'Defense Repository', 'North': 'Cargo Hold', 'South': 'Crystarium',
                             'item': 'Galactic Flight Manual'},
        'Cargo Hold': {'South': 'Knowledge Center', 'item': 'Shield'},
        'Crystarium': {'North': 'Knowledge Center', 'item': 'Crystal'},
        'Guards Chamber': {'South': 'Defense Repository', 'East': 'Control Room', 'item': 'Key'},
        'Control Room': {'item': 'Alien Commander'}
    }

    # start the player in the Prison Cells
    # set valid cardinal directions and create an empty dictionary to hold the inventory
    # call instructions function
    current_room = 'Prison Cells'
    valid_directions = ['North', 'South', 'East', 'West']
    inventory = []
    instructions()

    while True:
        status(current_room, inventory, rooms[current_room].get('item', 'empty'))
        if current_room == 'Control Room':  # check for game over condition
            print("\nUh Oh! It's the Alien Commander! Run! . . . Game Over!")
            print('Thank you for playing!')
            break
        if len(inventory) == 6:  # check for win condition
            print('\nYou found all the items and defeated the Alien Commander! Nice work!')
            print('Thank you for playing!')
            break

        user_input = input('Enter your move: \n')
        if user_input in valid_directions:
            new_room = rooms[current_room].get(user_input, 'You cannot go this way!')
            if new_room == 'You cannot go this way!':
                print(new_room, '\n')  # inform player of blocked direction
            else:
                current_room = new_room  # set current room to the new room
        elif user_input[0:3] == 'get':
            user_item = user_input[4:]
            if user_item == rooms[current_room].get('item'):
                inventory.append(user_item)
                del rooms[current_room]['item']
                print('You picked up the', user_item, '\n')
            else:
                print('You cannot get the', user_item, '\n')
        else:
            print('Invalid Response')


main()
