def Insertion_sort(array, n):
    for j in range(n):
        flag = j
        for k in range(j+1,n):
            if array[k] < array[flag]:
                flag = k
        t = array[j]
        array[j] = array[flag]
        array[flag] = t

def Quick_sort(array, i, j):
    if i == j:
        return
    if i == j-1:
        if array[j] < array[i]:
            t = array[j]
            array[j] = array[i]
            array[i] = t
        return
    s = i
    e = j
    p = array[s]
    i += 1
    while i < j:
        while array[i] < p:
            if i+1 <= e:
                i += 1
            else:
                break
        while array[j] > p:
            if j-1 >= s:
                j -= 1
            else:
                break
        if i < j:
            t = array[i]
            array[i] = array[j]
            array[j] = t
    array[s] = array[j]
    array[j] = p
    if j-1 > s:
        Quick_sort(array, s, j-1)
    if j+1 < e:
        Quick_sort(array, j+1, e)
while True:
    print("1.快速排序法", end=" ")
    print("2.插入排序法", end=" ")
    print("3.程式結束")
    select = input("請輸入選項：")
    if select == "3":
        break
    elif select !="1" and select != "2":
        print("請輸入 1 或 2 或 3")
        print("=============================================")
        continue
    
    try:
        print("從test1.txt讀到的數列：", end="")
        file = open('test1.txt', 'r')
        I = file.read().split()
        for i in I:
            print(i, end=" ")
        print("")
    except:
        I = input("找不到test1.txt，請以鍵盤輸入：")
        I = I.split()
    array = []
    for i in I:
        array.append(float(i))
    n = len(array)

    if select == "1":
        Quick_sort(array, 0, n-1)
        print("Quick Sort的結果：")
        for a in array:
            print(a, end=" ")
            
    elif select == "2":
        Insertion_sort(array, n)
        print("Insertion Sort的結果：")
        for a in array:
            print(a, end=" ")

    print("")
    print("共有",n,"個數")
    print("最大的數：",array[n-1])
    print("最小的數：", array[0])
    
    print("=============================================")