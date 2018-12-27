def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d24input.txt")
#lines = readFile("test.txt")

groups = None


def reset_groups():
    global groups

    groups = []
    id = 0
    for line in lines[1:11]:
    #for line in lines[1:3]:
        l1 = line.split(' ')
        units = int(l1[0])
        hp = int(l1[4])
        dmg = int(l1[-6])
        type = l1[-5]
        initiative = int(l1[-1])
        try:
            l2 = line[line.index('(')+1:line.index(')')]
            l3 = l2.split('; ')
            immune = []
            weak = []
            for part in l3:
                l4 = part.split(" ")[0]
                l5 = part[part.index("to") + 3:].split(", ")
                if l4 == "weak":
                    weak = l5
                elif l4 == "immune":
                    immune = l5
        except:
            immune = []
            weak = []
        power = units * dmg
        group = [id, 0, units, hp, immune, weak, dmg, type, initiative, power]
        groups.append(group)
        id += 1

    for line in lines[13:23]:
    #for line in lines[5:7]:
        l1 = line.split(' ')
        units = int(l1[0])
        hp = int(l1[4])
        dmg = int(l1[-6])
        type = l1[-5]
        initiative = int(l1[-1])
        try:
            l2 = line[line.index('(')+1:line.index(')')]
            l3 = l2.split('; ')
            immune = []
            weak = []
            for part in l3:
                l4 = part.split(" ")[0]
                l5 = part[part.index("to") + 3:].split(", ")
                if l4 == "weak":
                    weak = l5
                elif l4 == "immune":
                    immune = l5
        except:
            immune = []
            weak = []
        power = units * dmg
        group = [id, 1, units, hp, immune, weak, dmg, type, initiative, power]
        groups.append(group)
        id += 1


def calculate_damage(g1, g2):
    power = g1[-1]
    if g1[7] in g2[4]:
        return 0
    elif g1[7] in g2[5]:
        return 2 * power
    else:
        return power


def target_selection():
    global groups

    sorted_groups = groups[:]
    sorted_groups = sorted(sorted_groups, key=lambda x: (x[-1], x[-2]), reverse=True)
    targets = dict()
    targeted = dict()
    for i in range(len(sorted_groups)):
        g1 = sorted_groups[i]
        best_ind = None
        best_power = None
        for j in range(len(groups)):
            g2 = groups[j]
            if g1[1] != g2[1] and j not in targeted and g2[2] > 0:
                dmg = calculate_damage(g1, g2)
                if dmg == 0:
                    continue
                elif best_ind == None or dmg > best_power:
                    best_ind = j
                    best_power = dmg
                elif dmg == best_power:
                    prev_power = groups[best_ind][-1]
                    if g2[-1] > prev_power:
                        best_ind = j
                        best_power = dmg
                    elif g2[-1] == prev_power:
                        prev_init = groups[best_ind][-2]
                        if g2[-2] > prev_init:
                            best_ind = j
                            best_power = dmg
        targets[g1[0]] =  best_ind
        if best_ind is not None:
            targeted[best_ind] = 1
    return targets


def attack(targets, verbose=False):
    global groups

    sorted_groups = groups[:]
    sorted_groups = sorted(sorted_groups, key=lambda x: x[-2], reverse=True)
    for g1 in sorted_groups:
        if g1[2] > 0 and targets[g1[0]] is not None:
            g2 = groups[targets[g1[0]]]
            if verbose:
                print("Group {} is attacking Group {}".format(g1[0], g2[0]))
            dmg = calculate_damage(g1, g2)
            units_killed = dmg // g2[3]
            g2[2] = max(0, g2[2] - units_killed)
            g2[-1] = g2[2] * g2[6]
            if verbose:
                print("Dealt {} damage and killed {} units".format(dmg, units_killed))


def check_done():
    global groups
    winner = None
    count = 0
    for g in groups:
        if g[2] > 0:
            if winner is None:
                winner = g[1]
                count += g[2]
            else:
                if g[1] != winner:
                    return None, None
                else:
                    count += g[2]
    return count, winner


def print_groups():
    global groups
    print("------------------------")
    for g in groups:
        print(g)
    print("------------------------")


def apply_boost(boost):
    global groups
    for g in groups:
        if g[1] == 0:
            g[6] += boost
            g[-1] = g[2] * g[6]



print("Part 1")
reset_groups()
done = [None, None]
while done[0] is None:
    targets = target_selection()
    attack(targets, verbose=False)
    done = check_done()
print(done[0])


print()
print("Part 2")
boost_done = False
boost = 77
while not boost_done:
    reset_groups()
    apply_boost(boost)
    done = [None, None]
    while done[0] is None:
        targets = target_selection()
        attack(targets, verbose=False)
        done = check_done()

    if done[1] == 0:
        print(done[0])
        boost_done = True
    boost += 1
