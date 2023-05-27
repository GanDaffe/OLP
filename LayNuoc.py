def water():
    with open('Water.txt', 'r') as f: 
        lines = f.readlines()
    list_ = []
    nuoc, thung = 0, 0
    
    for i in range(1, len(lines)): 
        line = lines[i].split(' ')
        nuoc += int(line[0])
        thung += int(line[1])
        list_.append(int(line[1]))
    
    if nuoc == thung: 
        return 0
    
    list_.sort(reverse = True)
    c, i = thung - nuoc, 0
    
    while(c > 0): 
        c -= list_[i]
        i += 1

    return i
