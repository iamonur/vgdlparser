import os
import io
import itertools


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
    interaction.append(inter[0]) #interacter
    interaction.append(inter[1]) #interacter
    interaction.append(inter[3]) #interaction
    return interaction

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

def parse_main_functionality(filename):
    outcome = check(filename)[1]

    return_interactions = []
    return_terminations_w = []
    return_terminations_l = []

    q = 0
    for i in outcome:
        q += 1
        if i == "InteractionSet":
            return_interactions = passInteractions(outcome[q])
        elif i == "TerminationSet":
            return_terminations_w, return_terminations_l = passTerminations(outcome[q])

    return return_terminations_w, return_terminations_l, return_interactions


if __name__ == "__main__":

    i1, i2, i3 = parse_main_functionality("tests/pacman")
    print(i1)
    print(i2)
    print(i3)
