import os
import io
import itertools

def check2(filename):
    indentation = []
    indentation.append(0)
    depth = 0

    f = open("tests/aliens", 'r')

    for line in f:
        line = line[:-1]

        content = line.strip()
        indent = len(line) - len(content)
        if indent > indentation[-1]:
            depth += 1
            indentation.append(indent)

        elif indent < indentation[-1]:
            while indent < indentation[-1]:
                depth -= 1
                indentation.pop()

            if indent != indentation[-1]:
                raise RuntimeError("Bad formatting")

        print(content + " depth: " + str(depth))

def check(filename):
    data = []
    indentation = []
    indentation.append(0)
    depth = 0
    f = open(filename, 'r')

    for line in f:
        line = line[:-1]
        print(line)
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

if __name__ == "__main__":

    print(check("tests/aliens"))


#    content = open("tests/aliens")
#
#    stack = []
#    for line in content:
#        content = line.rstrip()  # drop \n
#        row = content.split("   ")
#        stack[:] = stack[:len(row) - 1] + [row[-1]]
#        print("\t".join(stack))
