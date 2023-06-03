def sinh(arr):
    i = n - 1 #Khoi tao bien i bang n - 1
    while i >= 0 and arr[i] == 1: #i chạy từ cuối đến đầu list, nếu phát hiện phần tử arr[i] = 1 thì trừ i = i - 1
        i -= 1 
    """
    Ví dụ [0, 0, 0, 0, 0, 0] vì mọi giá trị bằng 0 nên không thực hiện vòng lặp.
          [0, 0, 0, 0, 0, 1] i bắt đầu chạy từ vị trí thứ 6, đến vt thứ 5 gặp phần tử 0 thì dừng, lúc này i lấy giá trị = 5.
           1  2  3  4  5  6
    """
    
    arr[i] = 1 #chuyển i tại vị trí sau cùng thành giá trị 1
    
    for idx in range(i + 1, n):
        arr[idx] = 0
    """
    Ví dụ: 
          [0, 0, 0, 0, 1, 1] là mảng có được sau khi chuyển giá trị ở vị trí thứ 5 của mảng thành 1.
          lúc này i = 5, ta thực hiện chuyển i + 1 thành 0 được: 
          [0, 0, 0, 0, 1, 0] được trường hợp tiếp theo của dãy nhị phân
          
          Tương tự: 
          [0, 0, 0, 1, 1, 0]  -> [0, 0, 0, 1, 0, 0]
          có thể thay chỗ calcTime(arr) thành print(arr) để hiểu rõ cách chuyển hơn
          
    """
      
def Binary2(): 
    arr = [0] * n #Khoi tao mang co n so 0
    while not arr == [1] * n:
        #print(arr)
        calcTime(arr) #Tinh ket qua theo ham arr
        sinh(arr) #Sinh arr moi
        
    calcTime(arr)
    
def calcTime(bArr): 
    t1, t2 = 0, 0 
    for i in range(n): 
        if bArr[i] == 0:
            t1 += arr1[i]
        else: 
            t2 += arr2[i]
    
    tg = max(t1, t2) 
    list_.append((tg, bArr.copy())) #Các phần tử của list_ là các tuples có dạng (130, [1,0,1,0,0,1])
    

def xuli(arr): 
    a1, a2 = "", ""
    for i in range(n): #[1,0,1,0,1,1] 0 1 2 3 4 5
        if arr[i] == 0: 
            a1 += str(i + 1) + ' '
        else: 
            a2 += str(i + 1) + ' ' #0 + 1 = 1 -> 1
    return a1.strip(), a2.strip() #Hàm strip xóa khoảng trống ở đầu và cuối chuỗi: 'hello   ' + strip() == 'hello'

with open('INP.txt', 'r') as f: 
    lines = f.readlines()

n = int(lines[0])
list_ = []
arr1 = [int(i) for i in lines[1].split(' ')]
arr2 = [int(i) for i in lines[2].split(' ')]

Binary2()

w = min(list_, key = lambda k:k[0])
res1, res2 = xuli(w[1])

with open ('FileOut.O', 'w') as f1: 
    f1.write('{}\n{}\n{}'.format(w[0],res1,res2)) #Ghi kết quả ra file
