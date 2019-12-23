import os
import parsor

avatars = []

def addInteraction(interactions, interaction):
    for i in interactions:
        if i == interaction:
            return
    interactions.append(interaction)

#def registerAvatars(spritelist, initavatar):
 #   for s in spritelist:

        #for q in s:

  #      if isinstance(s, basestring):
   #         if s == initavatar:
    #            return True, s
     #   else:
      #      bl = registerAvatars(s, initavatar)
       #     if bl is True:
        #        print (s)
         #       return True, s
    #print avatars
    #return False

def registerAvatars(spritelist, initavatar):

	#print(spritelist)
	for a in spritelist:
		#print(a)
		if isinstance(a, basestring):
			if a == initavatar:
				return True, 0, a
			else:
				continue
		else:
			bl, inte, stri = registerAvatars(a, initavatar)
			if bl is True:
				if inte is 0:
					return True, 1, a
				elif inte is 1:
					return True, 1, stri
			else:
				continue
	return False, -1, spritelist

def parseAvatars(reg_avatars):
    #print(reg_avatars)
    reg_avatars = reg_avatars[0]
    avatars = []
    avatars.append(reg_avatars[0])
    for item in reg_avatars:
        if isinstance(item, basestring):
            continue
        else:               #avatar list
            for i in item:
		#print(i)
                avatars.append(i[0])
    #print (avatars)
    return avatars

#def addAvatar(avatars, interaction):
 #   new_avatar = interaction[-1].partition("=")[2]
  #  for avatar in avatars:
   #     if new_avatar == avatar:
    #        return false, avatars
    #avatars.append(new_avatar)
    #return true

def stateChecker(interactions, reg_avatars):
    avatars = []
    relatedInteractions = []
    for interaction in interactions:
        #print(interaction)
        if interaction[0] in reg_avatars or interaction[1] in reg_avatars:
            addInteraction(relatedInteractions, interaction)
            if interaction[2] == "transformTo":
            	interaction[3] = interaction[3].partition("=")[2]
    return relatedInteractions

def passAvatars(avatarStruct):
	ret = []
	for i in avatarStruct:
		if isinstance(i,int) or isinstance(i,bool):
			continue
		else:
			ret.append(i)
	#print (ret)
	return ret

def interpretor_main_functionality(filename, initialAvatar):
    winners = []
    losers = []
    interactions = []

    winners, losers, interactions, sprites = parsor.parse_main_functionality(filename)

    #print(sprites)
    avatars = parseAvatars(passAvatars(registerAvatars(sprites, initialAvatar)))
    relatedint = stateChecker(interactions, avatars)

    return winners, losers, relatedint, avatars

if __name__ == "__main__":
    for i in interpretor_main_functionality("tests/pacman", "pacman"):
        print(i)
