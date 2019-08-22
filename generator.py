"""A You Have 10 Seconds 3 unofficial expansion made by KikooDX
kikoodata.000webhostapp.com"""

from modules.loadRooms import *
from modules.createFrame import *
from modules.drawRoom import *
from modules.objects import *

def main(file_name="generated_level.yh10s3"):
    area_array = [1, 5, 8, 9, 10, 12, 15]
    area = choice(area_array)
    #area = 12
    
    r_tl, r_tr, r_dl, r_dr = loadRooms()
    print("Generation start")
    level, current_id = createFrame(area)
    print("Generation end")

    object_dict, levelinfo = objects(area)
    print("Area {}".format(area))

    x = 144
    y = 32

    for i in range(4):
        if i == 0:
            room_type = "start"
            r_tmp = r_tl
        if i == 1:
            room_type = None
            r_tmp = r_tr
            x += 112
        elif i == 2:
            room_type = "exit"
            r_tmp = r_dl
            x -= 112
            y += 112
        elif i == 3:
            room_type = None
            r_tmp = r_dr
            x += 112
        level, current_id = drawRoom(level, x, y, r_tmp, current_id, room_type, object_dict, area)

    level += levelinfo
    print("Saving level...\n")
    with open(file_name, "w") as file:
        file.write(level)

if __name__ == "__main__":
    file_name = input("Enter the name of the file to save in :\n> ")
    main(file_name)
    input("Level saved ! Press ENTER to exit this program.")