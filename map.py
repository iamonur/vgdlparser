import parsor

def checkMap(levelfile):
    f = open(levelfile, 'r').read()
    unique_chars = set(f)
    unique_chars.remove('\n')
    return unique_chars

def workOnMapping(mapping, levelfile):
    defaults = set()

    defaults.add('w') #Assume a wall for this
    defaults.add(' ') #Assume a floor for this
    defaults.add('.') #Assume a floor for this
    defaults.add('A') #Assume an avatar for this

    fromLevel = checkMap(levelfile)

    fromRules = set()
    for mapped in mapping:
        fromRules.add(mapped.partition('>')[0][:-1])

    if fromLevel.difference(fromRules.union(defaults)) != set():
        raise Exception('Non-suitable character in level mapping')

    toRetDef = fromLevel.difference(fromRules).intersection(defaults)

    return fromLevel, fromRules, toRetDef


def map_main_functionality(descfile, levelfile):

    outcome = parsor.check(descfile)
    q = 0
    outcome = outcome[1]
    for i in outcome:
        q += 1
        if i == "LevelMapping":
            return workOnMapping(outcome[q], levelfile)


if __name__ == "__main__":
    for i in map_main_functionality("tests/boulderdash/boulderdash_ruleset", "tests/boulderdash/boulderdash_level"):
        print(i)
