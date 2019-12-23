import interpretor

def generator_main_functionality(filename, avatarname):
    states = []
    statetransitions = []
    terminatingstates = []

    states.append(avatarname)
    startingstate = avatarname

    winning, losing, interaction = interpretor.interpretor_main_functionality(filename, avatarname)

    if winning != []:
        states.append("winning")

    for win in winning:
        if win[0] == "SpriteCounter":
            condition = [win[1], "*", "leq", win[2], "winning"]
        elif win[0] == "MultiSpriteCounter":
            condition = [win[1], win[2], "leq", win[3], "winning"]
        statetransitions.append(condition)

    if losing != []:
        states.append("losing")

    for lose in losing:
        if lose[0] == "SpriteCounter":
            condition = [lose[1], "*", "leq", lose[2], "losing"]
        elif lose[0] == "MultiSpriteCounter":
            condition = [lose[1], lose[2], "leq", lose[3], "losing"]
        statetransitions.append(condition)

    for inter in interaction:
        if inter[-1] == "transformTo":
            

if __name__ == "__main__":
