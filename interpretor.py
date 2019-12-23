import os
import parsor

avatars = []

def addInteraction(interactions, interaction):
    for i in interactions:
        if i == interaction:
            return
    interactions.append(interaction)

def registerAvatars(spritelist, initavatar):
    for s in spritelist:

        #for q in s:

        if isinstance(s, basestring):
            if s == initavatar:
                return True, s
        else:
            bl = registerAvatars(s, initavatar)
            if bl is True:
                print (s)
                return True, s
    print avatars
    return False

def parseAvatars(reg_avatars):
    #print(reg_avatars)
    avatars = []
    for item in reg_avatars:
        if isinstance(item, basestring):
            continue
        else:               #avatar list
            for i in item:
                avatars.append(i[0])
    #print (avatars)
    return avatars

def addAvatar(avatars, interaction):
    new_avatar = interaction[-1].partition("=")[2]
    for avatar in avatars:
        if new_avatar == avatar:
            return false, avatars
    avatars.append(new_avatar)
    return true

def stateChecker(interactions, reg_avatars):
    avatars = []
    relatedInteractions = []
    for interaction in interactions:
        #print(interaction)
        if interaction[0] in reg_avatars or interaction[1] in reg_avatars:
            addInteraction(relatedInteractions, interaction)
            if interaction[2] == "transformTo":
                flag = addAvatar(avatars, interaction)
                if flag == True:
                    relatedInteractions.append(stateChecker(interactions, avatar))
    return relatedInteractions

def interpretor_main_functionality(filename, initialAvatar):
    winners = []
    losers = []
    interactions = []

    winners, losers, interactions, sprites = parsor.parse_main_functionality(filename)

    print(sprites)
    avatars = parseAvatars(registerAvatars(sprites, initialAvatar))
    relatedint = stateChecker(interactions, avatars)

    return winners, losers, relatedint, avatars

if __name__ == "__main__":
    for i in interpretor_main_functionality("tests/pacman", "pacman"):
        print(i)
