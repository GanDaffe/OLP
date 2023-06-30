class Students: 
    name = ""
    msv = ""
    que_quan = ""
    diem_mon = []
    diem_tb = 0.0
    
    def __init__(self, name, msv, que_quan, diem_mon): 
        self.name = name
        self.msv = msv
        self.que_quan = que_quan 
        self.diem_mon = diem_mon.copy()
        self.diem_tb = 0.0
                
    def __str__(self):
        s = "Ten: %s\nMa sinh vien: %s\nQue quan: %s \nDiem TB: %.2f" %(self.name, self.msv, self.que_quan, self.diem_tb) 
        return s

def printList(list_):
    if list_ == []:
        print("Khong co!")
    else:
        for att in list_:
            print(att)
            print('--------------')
        
with open("DiemThi.txt") as f: 
    lines = f.readlines()

n, k = int(lines[0].split(' ')[0]), int(lines[0].split(' ')[1])

class_ = []
for i in range(1, n + 1):
    line = lines[i].split(';')
    sv = Students(None, None, None, [])
    
    setattr(sv, 'name', line[0])
    setattr(sv, 'msv', line[1])
    setattr(sv, 'que_quan', line[2])
        
    diem = [float(idx) for idx in line[3].split(' ')]
    setattr(sv, 'diem_mon', diem)
        
    class_.append(sv)

for st in class_: 
    setattr(st, 'diem_tb', sum(getattr(st, 'diem_mon')) / k)

dict_ = {}
dict_['Gioi'] = list(filter(lambda sv: getattr(sv, 'diem_tb') >= 8, class_))
dict_['Kha'] = list(filter(lambda sv: sv.diem_tb >= 6.5, [s for s in class_ if s not in dict_['Gioi']]))
dict_['Trung Binh'] = list(filter(lambda sv: sv.diem_tb >= 5, [s for s in class_ if s not in dict_['Gioi'] and s not in dict_['Kha']]))
dict_['Kem'] = [sv for sv in class_ if sv not in dict_['Gioi'] and sv not in dict_['Kha'] and sv not in dict_['Trung Binh']]

hn_good = list(filter(lambda sv: getattr(sv, 'diem_tb') >= 8 and getattr(sv, 'que_quan') == 'Ha Noi', dict_['Gioi']))

for key, values in dict_.items(): 
    print("Nhung hoc sinh co hoc luc", key.upper(), ": ")
    printList(values)
    input()

print("Nhung sinh vien co hoc luc gioi o Ha Noi: ") 
printList(hn_good)
