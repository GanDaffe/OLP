def generateBinary(length, bArr):
    if length == n: 
        calcTime(bArr) 
        return
    else: 
        bArr[length] = 0
        generateBinary(length + 1, bArr) 
        bArr[length] = 1
        generateBinary(length + 1, bArr)
    
def calcTime(bArr): 
    t1, t2 = 0, 0 
    for i in range(n): 
        if bArr[i] == 0:
            t1 += arr1[i]
        else: 
            t2 += arr2[i]
    
    tg = max(t1, t2) 
    res = bArr.copy()
    dic.append((tg, res))

def xuli(arr): 
    a1, a2 = [], []
    for i in range(n): 
        if arr[i] == 0: 
            a1.append(i + 1)
        else: 
            a2.append(i + 1)
    return a1, a2

with open('INP.txt', 'r') as f: 
    lines = f.readlines()
    
n = int(lines[0])
arr1 = [int(i) for i in lines[1].split(' ')]
arr2 = [int(i) for i in lines[2].split(' ')]

arr = n * [0]
dic = []
generateBinary(0, arr)
dic.sort(key = lambda k:k[0])
val = dic[0]

min_tg = val[0]
p_works, c_works = xuli(val[1]) 

print('{} \n{} {}'.format(min_tg, p_works, c_works))
