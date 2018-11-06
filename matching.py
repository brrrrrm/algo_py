s = ['Tom', 'Jerry', 'Eric', 'Mike','John', 'Eric']

def matchingTwo(a) :
    b = []
    c = []
    for i in range(len(a)) :
        for j in range(i+1, len(a)) :
            c = (a[i], a[j])
            b.append(c)

    return b
print(matchingTwo(s))