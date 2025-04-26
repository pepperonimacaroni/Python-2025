n = int(input('n = '))
arr = []

def nhap_db():
    global n, arr
    for i in range(n):
        print('A[', end='')
        print(i, end='')
        print('] = ', end='')
        tmp = int(input())
        arr.append(tmp)

    for i in range(n):
        print('A[', end='')
        print(i, end='')
        print('] = ', end='')
        print((arr[i]))

def bubble_sort():
    global n, arr
    for i in range(n):
        for j in range(1,i):
            if arr[j-1] > arr[j]:
                tmp = arr[j-1]
                arr[j-1]=arr[j]
                arr[j]=tmp
    print('========Xu Ly Xong========')
def xuat_kq():
    print('========Da Sap Xep========')
    for i in range(n):
        print(arr[i], end=" ")
nhap_db()
bubble_sort()
xuat_kq()