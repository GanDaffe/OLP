class Student: 
    tag = 1
    def __init__(self, name, que_quan, diem_thi = []): 
        self.name = name
        self.sid = f'%03d' %(Student.tag) 
        self.que_quan = que_quan 
        self.diem_thi = diem_thi
        self.hoc_luc = ''
        Student.tag += 1
        
    def __str__(self): 
        return f'Ten: %s\nMSV: %s\nQue quan: %s' %(self.name, self.sid, self.que_quan)
    
    def set_hoc_luc(self, hoc_luc): 
        self.hoc_luc = hoc_luc
        
class Manager: 
    def __init__(self,n = 1 , k = 1, students = []):
        self.students = students
        self.n = n 
        self.k = k
    
    def input(self):
        for i in range(self.n):
            name = input('Nhap ten: ')
            que_quan = input('Nhap que quan: ')
            
            ok = False
            while not ok: 
                diem_thi = input('Nhap diem cac mon, cach nhau 1 khoang trong: ')
                dem = 0
                for c in diem_thi.split(' '):
                    if c.isdigit(): 
                        dem += 1                
                if dem == k:
                    ok = True
                else:
                    print(f'Vui long nhap {k} diem!')
        
            sv = Student(chuan_hoa(name), chuan_hoa(que_quan), [float(i) for i in diem_thi.strip().split(' ')])
            self.students.append(sv)
            print('----------------')
    
    def chuan_hoa(str_arg):
        t = str_arg.strip().split(' ')
        if len(t) < 2: 
            return str_arg.capitalize()

        res = t[0].capitalize()
        for i in range(1, len(t)): 
            res += ' ' + t[i].capitalize()

        return res
    
    def get_students(self):
        return self.students
    
def printList(list_): 
    if list_ == []:
        print('Khong co!')
    else:
        for i in list_:
            print(i)
            print('----------')
    input()
    
if __name__ == '__main__':
    ok = False
    while not ok: 
        try: 
            n, k = int(input('Nhap so sinh vien: ')), int(input('Nhap so mon hoc: '))
            ok = True
        except ValueError: 
            print('Not OK')
            
    m = Manager(n, k)
    m.input()
    
    for sv in m.get_students(): 
        ave = sum(getattr(sv, 'diem_thi')) / k
        if ave >= 8.0:
            sv.set_hoc_luc('Gioi')
        elif ave >= 6.5:
            sv.set_hoc_luc('Kha')
        elif ave >= 5.0:
            sv.set_hoc_luc('Trung Binh')
        else: 
            sv.set_hoc_luc('Kem')
        
    print('Nhung hoc sinh co hoc luc gioi: ')
    printList(list(filter(lambda sv: getattr(sv, 'hoc_luc') == 'Gioi', m.get_students())))
    
    print('Nhung hoc sinh co hoc luc kha: ') 
    printList(list(filter(lambda sv: getattr(sv, 'hoc_luc') == 'Kha', m.get_students())))
    
    print('Nhung hoc sinh co hoc luc trung binh: ')
    printList(list(filter(lambda sv: getattr(sv, 'hoc_luc') == 'Trung Binh', m.get_students())))
    
    print('Nhung hoc sinh co hoc luc kem: ')
    printList(list(filter(lambda sv: getattr(sv, 'hoc_luc') == 'Kem', m.get_students())))
    
    print('Nhung hoc sinh co hoc luc gioi o ha noi: ')
    printList(list(filter(lambda sv: getattr(sv, 'hoc_luc') == 'Gioi' and getattr(sv, 'que_quan') == 'Ha Noi', m.get_students())))
