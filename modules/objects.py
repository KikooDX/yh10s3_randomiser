from random import choice

def objects():
    objet_dict = {"#" : ("75", 0, 0), #block
                  "v" : ("78", 0, 0), #spike
                  "<" : ("79", 0, 0), #left conveyor
                  ">" : ("80", 0, 0), #right conveyor
                  "~" : ("89", 0, 0)} #water

    level_infos = [54, "", 1, 0, 0] # music, title, BG, motion sensor, darkness
    # default is for Area 1

    area_array = [1, 5, 9, 10, 12, 15]
    area = choice(area_array)
    #area = 12

    if area == 5:
        level_infos = [58, "", 6, 0, 0]
    elif area == 9:
        level_infos = [62, "", 11, 1, 0] # laser
    elif area == 10:
        level_infos = [63, "", 14, 0, 0]
        objet_dict.update({"<" : ("97", 0, 0), # set red conveyors
                           ">" : ("98", 0, 0)})
    elif area == 12:
        level_infos = [65, "", 16, 0, 0]
        objet_dict.update({"<t" : ("100", 0, 0),
                           ">t" : ("100", 0, 0)}) # glue on conveyors
    elif area == 15:
        level_infos = [68, "", 31, 0, 1] # darkness

    levelinfo = "\n[levelinfo]\n"
    for i, info in enumerate(level_infos):
        levelinfo += "{}={}\n".format(i+1, info)

    return objet_dict, levelinfo, area