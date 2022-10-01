class Point:
    def __init__(self, x, y, rank, index):
        self.x, self.y = x, y
        self.rank = rank
        self.index = index


def heap_sort(p, t):
    def max_heap_x(r, n):
        root = r
        c = root * 2+1
        if c >= n:
            return

        if c + 1 < n and p[c].x < p[c+1].x:
            c += 1

        if p[c].x > p[root].x:
            p[root], p[c] = p[c], p[root]

        max_heap_x(c,n)

        

    def max_heap_y(r, n):
        root = r
        c = root * 2+1
        if c >= n:
            return

        if c + 1 < n and p[c].y < p[c+1].y:
            c += 1

        if p[c].y > p[root].y:
            p[root], p[c] = p[c], p[root]
        max_heap_y(c, n)

    def max_heap_r(r, n):
        root = r
        c = root * 2+1
        if c >= n:
            return

        if c + 1 < n and p[c].rank < p[c+1].rank:
            c += 1

        if p[c].rank > p[root].rank:
            p[root], p[c] = p[c], p[root]
        max_heap_r(c, n)

    def max_heap_i(r, n):
        root = r
        c = root * 2+1
        if c >= n:
            return

        if c + 1 < n and p[c].index < p[c+1].index:
            c += 1

        if p[c].index > p[root].index:
            p[root], p[c] = p[c], p[root]
        max_heap_i(c, n)

    n = int(len(p))
    if t == 'x':
        for i in range(n // 2, -1, -1):
            max_heap_x(i, n)
        for i in range(n-1, 0, -1):
            p[i], p[0] = p[0], p[i]
            max_heap_x(0, i)
    elif t == 'y':
        for i in range(n // 2, -1, -1):
            max_heap_y(i, n)
        for i in range(n-1, 0, -1):
            p[i], p[0] = p[0], p[i]
            max_heap_y(0, i)
    elif t == 'r':
        for i in range(n // 2, -1, -1):
            max_heap_r(i, n)
        for i in range(n-1, 0, -1):
            p[i], p[0] = p[0], p[i]
            max_heap_r(0, i)
    elif t == 'i':
        for i in range(n // 2, -1, -1):
            max_heap_i(i, n)
        for i in range(n-1, 0, -1):
            p[i], p[0] = p[0], p[i]
            max_heap_i(0, i)
    return p

def find_rank(s, e, point):
    m = int((s+e)/2)
    if e-s <= 1:
        return
    else:
        
        find_rank(s, m, point)
        find_rank(m, e, point)
        point[s:m] = heap_sort(point[s:m], 'y')
        point[m:e] = heap_sort(point[m:e], 'y')
        
        l = s
        r = m
        i = s
        c = 0
        while l < m and r < e:
            if point[l].y < point[r].y:  # 左<右
                l += 1
            elif point[l].y >= point[r].y:  # 左>右
                for i in range(s, l):
                    if point[i].x == point[r].x:
                        c += 1
                point[r].rank += l-s-c
                c = 0
                r += 1
        while r < e:
            for i in range(s, l):
                if point[i].x == point[r].x:
                    c += 1
            point[r].rank += l-s-c
            c = 0
            r += 1
        point[s:e] = heap_sort(point[s:e],'x')
        return


file = open('test2.txt', 'r')
I = file.read().split()
n = int(len(I)/2)
point = []
j = 0
for i in range(n):
    point.append(Point(float(I[i*2]), float(I[i*2+1]), 0, j))
    j+=1
point = heap_sort(point,'y')
point = heap_sort(point, 'x')
find_rank(0, n, point)
point = heap_sort(point,'i')
r_sum = 0
print("依輸入順序排序：")
for i in point:
    print("index : {:>3d}  x : {:8.2f}  y : {:8.2f}  rank : {:>3d}".format(i.index, i.x, i.y, i.rank))
    r_sum += i.rank
print("共有", n, "個點")
point = heap_sort(point,'r')
print("最大rank：", point[n-1].rank)
print("最小rank：", point[0].rank)
print("平均rank：{:5.2f} ".format(r_sum/n))
# 3 4 -1 1 3 -1 7 3 -5 -1 -2 5 6 -3 1 -3 -4 3 -2 -1 -7 -1 1 2 -3 1 5 3 -4 -3 -1 4 -1 -2 2 5 6 5
