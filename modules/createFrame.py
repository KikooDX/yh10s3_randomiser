def createFrame(area):
    here_id = 0
    lvl = "[save]\n"
    if area == 8:
        filler = "92"
    else:
        filler = "75"
    
    for h in range(2):
        if h == 0:
            y = 16
        else:
            y = 256
        for i in range(128, 384, 16):
            x = i
            for j in range(3):
                lvl += "{}{}=".format(here_id, j)
                if j == 0:
                    lvl += filler
                elif j == 1:
                    lvl += str(x)
                elif j == 2:
                    lvl += str(y)
                lvl += "\n"
            here_id += 1

    for h in range(2):
        if h == 0:
            x = 128
        else:
            x = 368
        for i in range(32, 244, 16):
            y = i
            for j in range(3):
                lvl += "{}{}=".format(here_id, j)
                if j == 0:
                    lvl += filler
                elif j == 1:
                    lvl += str(x)
                elif j == 2:
                    lvl += str(y)
                lvl += "\n"
            here_id += 1

    return lvl, here_id