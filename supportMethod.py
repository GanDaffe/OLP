#tim cac day con co k phan tu voi tong la lon nhat
def maxSubsequence(nums, k):
    arr = [(nums[i], i) for i in range(len(nums))]
    arr.sort(reverse=True)

    arr = arr[:k]
    arr.sort(key=lambda k: k[1])

    return [val[0] for val in arr]
#Tinh tong cac phan tu trong list co vi tri luu trong list 'index'
def getSum(nums, index):
    sum = 0
    for i in index:
        sum += nums[i - 1]
    return sum 
#Tong tu k den het cua list
def remainSum(nums, k):
    sum_ = 0    
    for i in range(k):
        sum_ += nums[i]
        
    return sum(nums) - sum_

def giaithua(n):
    if n == 0: 
        return 1
    dict_ = {}
    dict_[0] = 1
    for i in range(1, n + 1):
        dict_[i] = dict_[i - 1] * i
    return dict_[n]

def fibonaci(n):
    if n < 2: 
        return 1 
    dict_ = {}
    dict_[0] = 1
    dict_[1] = 1
    for i in range(2, n + 1): 
        dict_[i] = dict_[i - 1] + dict_[i - 2]
        
    return dict_[n]

#Thuật toán sinh dãy nhị phân độ dài n.
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
