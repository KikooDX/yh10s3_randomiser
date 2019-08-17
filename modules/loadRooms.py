from random import randint

def loadRooms():
    r_tl, r_tr, r_dl, r_dr = list(), list(), list(), list()

    # Read the number of rooms in each folder
    with open("rooms/tl/n.txt", "r") as file:
        n_tl = int(file.read())
    with open("rooms/tr/n.txt", "r") as file:
        n_tr = int(file.read())
    with open("rooms/dl/n.txt", "r") as file:
        n_dl = int(file.read())
    with open("rooms/dr/n.txt", "r") as file:
        n_dr = int(file.read())
    
    seed = str()
    for i in range(4):
        if i == 0:
            n_tmp, r_tmp, fldr = n_tl, r_tl, "tl"
        elif i == 1:
            n_tmp, r_tmp, fldr = n_tr, r_tr, "tr"
        elif i == 2:
            n_tmp, r_tmp, fldr = n_dl, r_dl, "dl"
        elif i == 3:
            n_tmp, r_tmp, fldr = n_dr, r_dr, "dr"
        n_room = randint(0, n_tmp - 1)
        print("{}/{}".format(n_room, n_tmp - 1))
        seed += str(n_room) + "-"
        with open("rooms/{}/{}.txt".format(fldr, n_room), "r") as file:
            r_tmp.append("".join(file.read().split("\n"))) #Format the files
    
    with open("seed.txt", "w") as file:
        file.write(seed[:-1])
    return r_tl[0], r_tr[0], r_dl[0], r_dr[0]

if __name__ == "__main__":
    sky_rooms, gnd_rooms, tmp, l = loadRooms()
    print(gnd_rooms)