from datetime import datetime

def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d04input.txt")

sort_lines = []
for line in lines:
    dt = line[1:17]
    dt_obj = datetime.strptime(dt, "%Y-%m-%d %H:%M")
    p_line = [dt_obj, line[19:]]
    sort_lines.append(p_line)
sort_lines = sorted(sort_lines, key=lambda sort_lines: sort_lines[0])

asleep = False
gnum = 0
sleep_mins = dict()
sleep_min_maxes = dict()
slept = 0

def update_dicts(gnum, start, end):
    if gnum not in sleep_mins:
        sleep_mins[gnum] = 0
        sleep_min_maxes[gnum] = [0] * 60
    sleep_mins[gnum] += abs(end - start)
    i = start
    while i != end:
        sleep_min_maxes[gnum][i] += 1
        i = (i + 1) % 60

for line in sort_lines:
    minute = line[0].minute
    l1 = line[1].split(" ")
    if l1[0] == "Guard":
        if asleep:
            asleep = False
            update_dicts(gnum, slept, minute)
        gnum = int(l1[1][1:])
    elif l1[0] == "falls":
        asleep = True
        slept = minute
    elif l1[0] == "wakes" and asleep:
        asleep = False
        update_dicts(gnum, slept, minute)

max_elf = max(sleep_mins, key=sleep_mins.get)
max_minute = sleep_min_maxes[max_elf].index(max(sleep_min_maxes[max_elf]))

print(max_elf)
print(max_elf * max_minute)

max_max_val = 0
max_max_minute = 0
max_max_elf = 0
for elf in sleep_min_maxes:
    val = max(sleep_min_maxes[elf])
    ind = sleep_min_maxes[elf].index(val)
    if val > max_max_val:
        max_max_val = val
        max_max_minute = ind
        max_max_elf = elf

print(max_max_minute * max_max_elf)
