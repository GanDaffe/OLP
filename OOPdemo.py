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
    
def chuan_hoa(ten):
    t = ten.strip().split(' ')
    if len(t) < 2: 
        return ten.capitalize()
    
    res = t[0].capitalize()
    for i in range(1, len(t)): 
        res += ' ' + t[i].capitalize()
            
    return res

def printList(list_):
    if list_ == []:
        print("Khong co!")
    else:
        for att in list_:
            print(att)
            print('--------------')

n, k = int(input('Nhap so sinh vien: ')), int(input('Nhap so mon hoc: '))
input()

class_ = []
for i in range(n):
    sv = Students(None, None, None, [])
    
    setattr(sv, 'name', chuan_hoa(input('Nhap ten: ')))
    setattr(sv, 'msv', input('Nhap ma sinh vien: '))
    setattr(sv, 'que_quan', chuan_hoa(input('Nhap que quan: ')))
    
    diem = []
    for j in range(k):
        diem.append(float(input(f'Nhap diem mon thu {j + 1}: ')))
    
    setattr(sv, 'diem_mon', diem)
    class_.append(sv)
    
    print('-------------')

for sv in class_:
    setattr(sv, 'diem_tb', sum(getattr(sv, 'diem_mon')) / k)
    
dict_ = {}
dict_['Gioi'] = [sv for sv in class_ if getattr(sv, 'diem_tb') >= 8.0]
dict_['Kha'] = [sv for sv in class_ if getattr(sv, 'diem_tb') >= 6.5 and getattr(sv, 'diem_tb') < 8]
dict_['Trung Binh'] = [sv for sv in class_ if getattr(sv, 'diem_tb') >= 5.0 and getattr(sv, 'diem_tb') < 6]
dict_['Kem'] = [sv for sv in class_ if sv not in dict_['Gioi'] and sv not in dict_['Kha'] and sv not in dict_['Trung Binh']]

hn_good = [sv for sv in dict_['Gioi'] if getattr(sv, 'que_quan') == 'Ha Noi']

for key, val in dict_.items(): 
    print('Nhung sinh vien co hoc luc ', key.upper(), ': ')
    printList(val)
    input()
    
print('Nhung hoc sinh co hoc luc GIOI o Ha Noi: ')
printList(hn_good)
