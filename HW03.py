class line:
    def __init__(self, dis, road, way):
        self.dis, self.road, self.way = dis, road, way


f = []
d = []


def dijk(a, start, last, end, w, n, path, c):
    min = float('inf')
    min_index = start
    for i in range(n):
        if i in f:
            continue
        if(a[start][i].dis < d[i] or d[last]+a[last][i].dis < d[i]):
            if(a[start][i].dis <= d[last] + a[last][i].dis):
                if a[start][i].way[5-w] == "1" and a[start][i].dis < d[i]:
                    d[i] = a[start][i].dis
                    path[i] = start
                elif a[last][i].way[5-w] == "1" and d[last]+a[last][i].dis < d[i]:
                    d[i] = d[last] + a[last][i].dis
                    path[i] = last
            elif (a[start][i].dis > d[last] + a[last][i].dis):
                if a[last][i].way[5-w] == "1" and d[last]+a[last][i].dis < d[i]:
                    d[i] = d[last] + a[last][i].dis
                    path[i] = last
                elif a[start][i].way[5-w] == "1" and a[start][i].dis < d[i]:
                    d[i] = a[start][i].dis
                    path[i] = start

        if d[i] < min:
            min = d[i]
            min_index = i
    if min_index != start:
        f.append(min_index)
    if c != n:
        c += 1
        dijk(a, start, min_index, end, w, n, path, c)


file = open('test3.txt', 'r')
file2 = open('t2_out.txt', 'w')
I = []
for i in file:
    I.append(i)
n = int(I[0])
a = [[None]*n for i in range(n)]
path = [None]*n
for i in range(1, len(I)):
    t = I[i].split()
    x = int(t[0])
    y = int(t[1])
    dis = float(t[2])
    road = float(t[3])
    if x == y:
        print("輸入不可有self-loop")
        exit()
    if dis <= 0 or road <= 0:
        print("輸入距離和路幅不可<=0")
        exit()
    if x >= n or y >= n:
        print("輸入的點不符合規定")
        exit()
    if len(t) > 4:
        if road < 0.5:
            way = "00000"
        elif road < 1.5:
            way = "0000"+t[4][4]
        elif road < 2:
            way = "000"+t[4][3:5]
        elif road < 4:
            way = "00"+t[4][2:5]
        elif road < 6:
            way = "0"+t[4][1:5]
        else:
            way = t[4]
    else:
        if road > 6:
            way = "11111"
        elif road > 4:
            way = "01111"
        elif road > 2:
            way = "00111"
        elif road > 1.5:
            way = "00011"
        elif road > 0.5:
            way = "00001"
        else:
            way = "00000"
    a[x][y] = line(dis, road, way)

for i in range(n):
    for j in range(n):
        if(a[i][j] == None):
            a[i][j] = line(float('inf'), 0, "00000")

r = input("請輸入來源節點 目的節點 交通方式：").split()
if r[2] == "5":
    s = "巴士"
elif r[2] == "4":
    s = "轎車"
elif r[2] == "3":
    s = "機車"
elif r[2] == "2":
    s = "腳踏車"
elif r[2] == "1":
    s = "步行"
for i in range(n):
    d.append(float('inf'))
f.append(int(r[0]))
dijk(a, int(r[0]), int(r[0]), int(r[1]), int(r[2]), n, path, 0)
if d[int(r[1])] == float('inf'):
    print("無法到達")
    file2.write("無法到達")
else:
    final = [int(r[1])]
    j = int(r[1])
    while(1):
        if j == int(r[0]):
            break
        final.append(path[j])
        j = path[j]
    l = (len(final))
    final.reverse()
    print("總距離：", d[int(r[1])])
    file2.write("總距離："+str(d[int(r[1])])+"\n")
    print(s, "從 ", x, " 到 ", y, "的路徑：")
    file2.write(s+"從 "+str(x)+" 到 "+str(y)+"的路徑：\n")
    for i in range(l-1):
        x = final[i]
        y = final[i+1]
        print("從 ", x, " 到 ", y, " 距離：", a[x][y].dis, " 路幅：", a[x][y].road, " 通行限制：", a[x][y].way)
        file2.write("從 "+str(x)+" 到 "+str(y)+" 距離：" + str(a[x][y].dis) + " 路幅："+str(a[x][y].road) + " 通行限制："+a[x][y].way+"\n")
