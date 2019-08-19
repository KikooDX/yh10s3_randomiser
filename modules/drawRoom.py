def drawRoom(level, start_x, start_y, room, current_id, room_type, objet_dict, area):
    output = level
    i = 0
    banned_objects = "."
    if area == 5:
        banned_objects += "~"
    for y in range(start_y, start_y + 112, 16):
        for x in range(start_x, start_x + 112, 16):
            for j in range(2):
                objet = room[i]
                offset_x = 0
                offset_y = 0
                draw = True
                if j == 1:
                    objet += "t"
                if objet not in banned_objects:
                    draw = False
                    if objet in objet_dict:
                        objet = objet_dict[objet]
                        offset_x = objet[1]
                        offset_y = objet[2]
                        objet = objet[0]
                        draw = True
                    elif objet == "s":
                        if room_type == "start":
                            objet = "77"
                            offset_x = 8
                            draw = True
                        elif room_type == "exit":
                            objet = "76"
                            offset_x = 8
                            draw = True
                    if draw:
                        output += "{0}0={3}\n{0}1={1}\n{0}2={2}\n".format(current_id, x + offset_x, y + offset_y, objet)
                        current_id += 1
            if area == 5: # add a water overlay to the level
                output += "{0}0=89\n{0}1={1}\n{0}2={2}\n".format(current_id, x, y)
                current_id += 1
            i += 1
    return output, current_id
