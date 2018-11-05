s = ['Tom', 'Jerry', 'Mike','Tom','Apple','Mike', 'Apple', 'Tom']

def find_samename(list) :
    newSet = []
    for a in range(len(list)) :
        for b in range(a + 1, len(list)) :
            if list[a] == list[b]:
                newSet.append(list[a])
    return newSet

print(find_samename(s))

def find_samename2(list) :
    newSet = set()
    for a in range(len(list)) :
        for b in range(a + 1, len(list)) :
            if list[a] == list[b]:
                newSet.add(list[a])
    return newSet

print(find_samename2(s))