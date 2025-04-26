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

def insertion_sort():
    global n, arr
    for i in range (1,n):
        last = arr[i]
        j = i
        while j>0 and arr[j-1]< last:
            arr[j]=arr[j-1]
            j=j-1
        arr[j] = last
    print('========Xu Ly Xong========')
def xuat_kq():
    print('========Da Sap Xep========')
    for i in range(n):
        print(arr[i], end=" ")
nhap_db()
insertion_sort()
xuat_kq()
