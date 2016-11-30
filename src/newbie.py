# first solve
def find(computers, *minutes):
    min_list = list(minutes)
    min_list.sort(reverse=True)

    total = get_total(min_list)
    avg = total / computers
    result = []
    for x in range(computers):
        result.append([])

    for num in range(0, computers):
        for each in min_list:
            if avg >= get_total(result[num]) + each:
                index = min_list.index(each)
                result[num].append(min_list[index])
            else:
                if not result[num]:
                    result[num].append(each)
                    min_list.remove(each)
                    break
                else:
                    min_list.remove(result[num][-1])

    print result


def get_total(min_list):
    result = 0
    if not min_list:
        return result
    for n in min_list:
        result += n
    return result

# find(2, 5, 7, 1, 2, 3)
find(3, 3,15,6,22,13,2)

# someone's solve
def prg2com(inlist, coms):
    outlist = []
    sumout = []
    for x in range(coms):
        outlist.append([])
        sumout.append(0)

    inlist.sort(reverse=True)

    for bread in inlist:
        lowbasket = sumout.index(min(sumout))
        outlist[lowbasket].append(bread)
        sumout[lowbasket] += bread

    return outlist

print prg2com([3,15,6,22,13,2], 3)
