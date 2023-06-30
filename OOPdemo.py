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
            
def chuan_hoa(ten):
    t = ten.strip().split(' ')
    if len(t) < 2: 
        return ten.capitalize()
    
    res = t[0].capitalize()
    for i in range(1, len(t)): 
        res += ' ' + t[i].capitalize()
            
    return res     

class_ = []
n, k = int(input("Nhap so hoc sinh: ")), int(input("Nhap so mon hoc: "))

input()
for i in range(n):
    sv = Students(None, None, None, [])
    
    setattr(sv, 'name', chuan_hoa(input("Nhap ten: ")))
    setattr(sv, 'msv', input("Nhap ma sinh vien: "))
    setattr(sv, 'que_quan', chuan_hoa(input("Nhap que quan: ")))
    
    diem = []
    for j in range(k):
        diem.append(float(input(f"Nhap diem thi mon thu {j + 1}:")))
        
    setattr(sv, 'diem_mon', diem)
    print('--------------')
    class_.append(sv)
    
for st in class_: 
    setattr(st, 'diem_tb', sum(getattr(st, 'diem_mon')) / k)
 

#gioi = list(filter(lambda sv: getattr(sv, 'diem_tb') >= 8, class_))
gioi = []
for sv in class_:
    if sv.diem_tb >= 8: 
        gioi.append(sv)

kha = []
for sv in [i for i in class_ if i not in gioi]:
    if sv.diem_tb >= 6.5: 
        kha.append(sv)

tb = []
for sv in [i for i in class_ if i not in gioi and i not in kha]:
    if sv.diem_tb >= 5: 
        tb.append(sv)

kem = [sv for sv in class_ if sv not in gioi and sv not in kha and sv not in tb]

hn_good = []
for sv in gioi:
    if sv.que_quan == 'Ha Noi':
        hn_good.append(sv)

print("Nhung hoc sinh co hoc luc GIOI: ")
printList(gioi)
input()

print("Nhung hoc sinh co hoc luc KHA: ")
printList(kha)
input()

print("Nhung hoc sinh co hoc luc TRUNG BINH: ")
printList(tb)
input()

print("Nhung hoc sinh co hoc luc KEM: ")
printList(kem)
input()


print("Nhung sinh vien co hoc luc gioi o ha noi: ") 
printList(hn_good)
