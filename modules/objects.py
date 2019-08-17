from random import randint

def objects():
    objet_dict = {"#" : ("75", 0, 0), #block
                  "v" : ("78", 0, 0), #spike
                  "<" : ("79", 0, 0), #left conveyor
                  ">" : ("80", 0, 0), #right conveyor
                  "~" : ("89", 0, 0)} #water

    level_infos = [54, "", 1, 0, 0] # music, title, BG, motion sensor, darkness
    # default is for Area 1

    area_array = [1, 5, 9, 10]
    area_array = [5]
    area = area_array[randint(0, len(area_array)-1)]

    if area == 5:
        level_infos = [58, "", 6, 0, 0]
    elif area == 9:
        level_infos = [62, "", 11, 1, 0]
    elif area == 10:
        level_infos = [63, "", 14, 0, 0]
        objet_dict.update({"<" : ("97", 0, 0), # set red conveyors
                           ">" : ("98", 0, 0)})

    levelinfo = "\n[levelinfo]\n"
    for i, info in enumerate(level_infos):
        levelinfo += "{}={}\n".format(i+1, info)

    return objet_dict, levelinfo, area