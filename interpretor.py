import os
import parsor

avatars = []

def addInteraction(interactions, interaction):
    for i in interactions:
        if i == interaction:
            return
    interactions.append(interaction)

def addAvatar(avatars, interaction):
    new_avatar = interaction[-1].partition("=")[2]
    for avatar in avatars:
        if new_avatar == avatar:
            return false, avatars
    avatars.append(new_avatar)
    return true

def stateChecker(interactions, originalAvatar):
    avatars.append(originalAvatar)
    relatedInteractions = []
    for interaction in interactions:
        if interaction[0] == originalAvatar or interaction[1] == originalAvatar:
            addInteraction(relatedInteractions, interaction)
            if interaction[2] == "transformTo":
                flag = addAvatar(avatars, interaction)
                if flag == True:
                    relatedInteractions.append(stateChecker(interactions, avatar))
    return relatedInteractions

if __name__ == "__main__":


    w = []
    l = []
    i = []

    w, l, i = parsor.parse_main_functionality("tests/pacman")


    print(stateChecker(i, "pacman"))
