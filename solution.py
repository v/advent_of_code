import fileinput

def part1():
    cal_count = 0
    counts = []

    for line in fileinput.input():
        line = line.strip()

        if line == '':
            counts.append(cal_count)
            cal_count = 0
        else:
            cal_count += int(line)

    counts.append(cal_count)
    return max(counts)

def part2():
    cal_count = 0
    counts = []

    for line in fileinput.input():
        line = line.strip()

        if line == '':
            counts.append(cal_count)
            cal_count = 0
        else:
            cal_count += int(line)

    counts.append(cal_count)
    counts.sort(reverse=True)
    return sum(counts[:3])


print(part1())
print(part2())