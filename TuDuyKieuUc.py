def asignment(v, path): 
    if v == end1 or v == end2: 
        xuli(path)
    for nx in dic[v]:
        asignment(nx, path + [nx])
    
    
def xuli(arr): 
    a1, a2 = [], []
    s1, s2 = "", ""
    for i in range(ep): 
        if arr[i][2] == 1: 
            a1.append(arr[i][1])
            s1 += str(i + 1) + ' '
        else: 
            a2.append(arr[i][1])
            s2 += str(i + 1) + ' '
    
    tg = max(sum(a1), sum(a2))
    output.append((tg, s1.strip(), s2.strip()))
    

with open('INP.txt', 'r') as f: 
    lines = f.readlines()

ep = int(lines[0])
arr1 = [(i + 1, int(lines[1].split(' ')[i]), 1) for i in range(len(lines[1].split(' ')))]
arr2 = [(i + 1, int(lines[2].split(' ')[i]), 2) for i in range(len(lines[2].split(' ')))]
list_ = arr1 + arr2
 
list_.sort(key = lambda k:k[0])
dic = {}

for i in list_: 
    dic[i] = [t for t in list_ if t[0] == i[0] + 1]
    
output = []

end1 = list_[ep * 2 - 1]
end2 = list_[ep * 2 - 2] 
asignment(list_[0], [list_[0]])
asignment(list_[1], [list_[1]])

ans = min(output, key = lambda k: k[0])
print(ans)

with open('OUT.txt', 'w') as f1: 
    f1.write('{}\n{}\n{}'.format(ans[0], ans[1], ans[2]))
