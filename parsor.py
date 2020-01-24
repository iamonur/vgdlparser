import os
import io
import itertools

#Onur Tekik
def check(filename):
    data = []
    indentation = []
    indentation.append(0)
    depth = 0
    f = open(filename, 'r')

    for line in f:
        line = line[:-1]
        content = line.strip()
        indent = len(line) - len(content)
        #print (str(indent))
        if indent > indentation[-1]:
            depth += 1
            indentation.append(indent)
            data.append([])

        elif indent < indentation[-1]:
            while indent < indentation[-1]:
                depth -= 1
                indentation.pop()
                top = data.pop()
                data[-1].append(top)

            if indent != indentation[-1]:
                raise RuntimeError("Ruleset not quite OK formatted dude.")
        data[-1].append(content)

    while len(data) > 1:
        top = data.pop()
        data[-1].append(top)

    return data[0]

def parseTermination(term):
    termination = []
    termination.append(term[0])

    if term[0] == "SpriteCounter":
        termination.append(term[1].partition("=")[2]) #stype = n
        termination.append(term[2].partition("=")[2]) #limit = n

    elif term[0] == "MultiSpriteCounter":
        termination.append(term[1].partition("=")[2]) #stype1 = n
        termination.append(term[2].partition("=")[2]) #stype2 = n
        termination.append(term[3].partition("=")[2]) #limit = n

    if term[-1] == "win=False":
        return True, termination
    else:
        return False, termination

def parseInteraction(inter):
    interaction = []
    for i in inter:
        if i == '>':
            continue
        else:
            interaction.append(i)
    return interaction

def parseSprites(spr):
    sprite = []
    for i in spr:
        if i == '>':
            continue
        else:
            sprite.append(i)
    return sprite

def passTerminations(terminationSet):
    winning = []
    losing = []
    for i in terminationSet:
        boolean, term = parseTermination(i.split())
        if(boolean == 1):
            winning.append(term)
        else:
            losing.append(term)

    return winning, losing

def passInteractions(interactionSet):
    interactions = []
    for i in interactionSet:
        interactions.append(parseInteraction(i.split()))
    return interactions

def passSprites(spriteSet):
    sprites = []
    q = 0
    for s in spriteSet:
        if isinstance(s, basestring):
            sprites.append(parseSprites(s.split()))
        else:
            sprites[q-1].append(passSprites(s))
    return sprites

def parse_main_functionality(filename):
    outcome = check(filename)[1]

    return_interactions = []
    return_terminations_w = []
    return_terminations_l = []
    return_sprites = []

    q = 0
    for i in outcome:
        q += 1
        if i == "InteractionSet":
            return_interactions = passInteractions(outcome[q])
        elif i == "TerminationSet":
            return_terminations_w, return_terminations_l = passTerminations(outcome[q])
        elif i == "SpriteSet":
            return_sprites = passSprites(outcome[q])

    return return_terminations_w, return_terminations_l, return_interactions, return_sprites


if __name__ == "__main__":

    i1, i2, i3, i4 = parse_main_functionality("tests/pacman")
    for a in i4:
        print(a)
