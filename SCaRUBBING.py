import sys
print ("""<-----RULES----->
1. BRUSH DOWN
2. BRUSH UP
3. VEHICLE ROTATES RIGHT                     
4. VEHICLE ROTATES LEFT
5. MOVE UP TO X
6. JUMP
7. REVERSE DIRECTION
8. VIEW THE MATRIX
0. EXIT
Please enter the commands with plus sign (+) between them.""")

commands = input()
command_list = commands.split("+")
list_without_5 = [i for i in command_list if not i.startswith("5_")]

for i in list_without_5[1:]:
    if i.isdigit() == False:
        print("You entered an incorrect command.Please try again!")
        commands = input()
        command_list = commands.split("+")
        list_without_5 = [i for i in command_list if not i.startswith("5_")]
    elif int(i)>8:
        print("You entered an incorrect command.Please try again!")
        commands = input()
        command_list = commands.split("+")
        list_without_5 = [i for i in command_list if not i.startswith("5_")]

command_list = [int(i) for i in command_list]
position_x = 0
position_y = 0
direction = 0
brush = False
output = [[" "]*command_list[0] for i in range(command_list[0])]

def rotation(command):
    global direction                        # 0 is right
    if command == 3:                        # 1 is down
        direction += 1                      # 2 is left
    elif command == 4:                      # 3 is up
        direction -= 1
    elif command == 7:
        direction += 2
    direction = direction%4

def movement(unit):
    global position_x
    global position_y
    if direction == 0:
        for i in range(unit):
            position_x += 1
            position_x = position_x % command_list[0]
            if brush == True:
                output[position_y][position_x] = "*"
    elif direction == 1:
        for i in range(unit):
            position_y += 1
            position_y = position_y % command_list[0]
            if brush == True:
                output[position_y][position_x] = "*"
    elif direction == 2:
        for i in range(unit):
            position_x -= 1
            position_x = position_x % command_list[0]
            if brush == True:
                output[position_y][position_x] = "*"
    elif direction == 3:
        for i in range(unit):
            position_y -= 1
            position_y = position_y % command_list[0]
            if brush == True:
                output[position_y][position_x] = "*"

def jump():
    global direction
    global brush
    global position_x
    global position_y
    brush = False
    if direction == 0:
        position_x += 3
    elif direction == 1:
        position_y += 3
    elif direction == 2:
        position_x -=3
    elif direction ==3:
        position_y -=3

for i in command_list[1:]:
    if brush == True:
        output[position_y][position_x] = "*"
    if i == 1:
        brush = True
    elif i == 2:
        brush = False
    elif i == 3:
        rotation(3)
    elif i == 4:
        rotation(4)
    elif str(i).startswith("5"):
       movement(int(str(i)[1:]))
    elif i == 6:
        jump()
    elif i == 7:
        rotation(7)
    elif i == 8:
        print("+"*(command_list[0]+2))
        for y in range(0, command_list[0]):
            print("+",end="")
            for x in range(0, command_list[0]):
                print(output[y][x],end='')
            print("+")
        print("+" * (command_list[0] + 2))
    elif i == 0:
        sys.exit()