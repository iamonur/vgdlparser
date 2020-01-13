import interpretor

def generator_main_functionality(filename, avatarname):
    states = []
    statetransitions = []
    terminatingstates = []
    avatars = []

    states.append(avatarname)
    startingstate = avatarname

    winning, losing, interaction, avatars = interpretor.interpretor_main_functionality(filename, avatarname)

    if winning != []:
        states.append("winning")

    for win in winning:
        if win[0] == "SpriteCounter":
            condition = [win[1], "*", "winning"]
        elif win[0] == "MultiSpriteCounter":
            condition = [win[1], win[2], "winning"]
        statetransitions.append(condition)

    if losing != []:
        states.append("losing")

    for lose in losing:
        if lose[0] == "SpriteCounter":
            condition = [lose[1], "*", "losing"]
        elif lose[0] == "MultiSpriteCounter":
            condition = [lose[1], lose[2], "losing"]
        statetransitions.append(condition)

    for inter in interaction:
        if inter[2] == "transformTo":
            condition = [inter[0], inter[1], inter[3]]
            statetransitions.append(condition)
    return statetransitions



if __name__ == "__main__":
    print (generator_main_functionality("tests/pacman", "pacman"))
