

import subprocess

alternate_tick = ("X","O","X","O","X","O","X","O","X")

coun = "y"
def replace_all_value_array(array,old_value,new_value):
    dimension = len(array[0])
    for i in range(dimension):
        for j in range(dimension):
            if array[i][j] == old_value:
                array[i][j] = new_value

def tick_action(alt,position, array):
    replace_all_value_array(array,position,alt)

def display_table(array):
    a, b, c = 1, 2, 3
    temp = [["-", "-", "-"],
                     ["-", "-", "-"],
                     ["-", "-", "-"]]
    subprocess.run("cls",shell=True)
    print("Minigame: Tik Tac Toe"
          "\nChoosing the number equivalent to position you want to tick."
          "\n""The \"X\" is the 1st player!"
          "\nLet's goooo!"
          "\n-----------------------")
    for x in range(len(map_to_tick[0])):
        for y in range(len(map_to_tick[0])):
            if array[x][y] in ["X","O"]:
                temp[x][y] = array[x][y]
    for row in temp:
        print("{} | {} | {}     {} | {} | {}".format(row[0], row[1], row[2], a, b, c))
        a +=3
        b +=3
        c +=3
    print("-----------------------")

def is_win(array):
    X_win = ["X","X","X"]
    O_win = ["O","O","O"]
    temp = []
    temp = []
    diagonal_1 = []
    diagonal_2 = []
    dimesion = len(array[0])
    # get row
    for row in array:
        temp.append(row)
    # get column
    for i in range(dimesion):
        temp_col = []
        for j in range(dimesion):
            temp_col.append(array[j][i])
        temp.append(temp_col)
    # get first diagonal
    for i in range(dimesion):
        diagonal_1.append(array[i][i])
    temp.append(diagonal_1)
    # get second diagonal
    for i in range(dimesion):
        diagonal_2.append(array[dimesion - 1 - i][i])
    temp.append(diagonal_2)
    if (X_win in temp) or (O_win in temp):
        return True
    return False

def covert_array_list(array):
    temp = []
    for i in array:
        for j in i:
            temp.append(j)
    return temp

while coun == "y":
    map_to_tick = [['1', '2', '3'],
                            ['4', '5', '6'],
                            ['7', '8', '9']]
    round = 0
    display_table(map_to_tick)
    for alt in alternate_tick:
        round += 1
        position = input(f"Enter [exit] to escape. \n"
                         f"The \"{alt}\" player choose: ").upper()
        if position == "EXIT": exit()
        while not ((position in covert_array_list(map_to_tick)) and (position not in ("X","O"))):
            subprocess.run("cls", shell=True)
            display_table(map_to_tick)
            position = input(f"Enter [exit] to escape. \n"
                             f"The \"{alt}\" player should choose again: ").upper()
            if position == "EXIT": exit()
        # subprocess.run("cls",shell=True)
        tick_action(alt,position,map_to_tick)
        display_table(map_to_tick)
        if is_win(map_to_tick):
            print(f"The \"{alt}\" player WIN!"
                  f"\nCongatulation!")
            coun = input("Do you want to countinue? [Y]es or [N]o: ").lower()
            if coun == "y":
                break
            else:
                break
        if round == 9:
            print("A inconclusive game! ")
            coun = input("Do you want to countinue? [Y]es or [N]o: ").lower()
            if coun == "y":
                break
            else:
                break













