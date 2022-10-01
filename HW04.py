import sys #用於整數最大值
import copy #用於deepcopy

#建立樹的節點結構
class Tree:
    def __init__(self):
        self.lb = None
        self.f = None
        self.t = None
        self.left = None
        self.right = None
        self.cost = None 
        self.level = None

min_LB = sys.maxsize
num = 0

# 計算LB、reduce cost matrix
def LowerBound(LB, cost):
    n = len(cost)
    # row
    for i in range(n):
        min = sys.maxsize
        d = False
        for j in range(n):
            if i == j or cost[i][j] < 0:
                continue
            if cost[i][j] == 0:
                d = True
                break
            if cost[i][j] < min:
                min = cost[i][j]
        if d:
            continue
        for j in range(n):
            if i == j or cost[i][j] < 0:
                continue
            cost[i][j] -= min
        if min < sys.maxsize:
            LB += min
    # column
    for i in range(n):
        min = sys.maxsize
        d = False
        for j in range(n):
            if i == j or cost[j][i] < 0:
                continue
            if cost[j][i] == 0:
                d = True
                break
            if cost[j][i] < min:
                min = cost[j][i]
        if d:
            continue
        for j in range(n):
            if i == j or cost[j][i] < 0:
                continue
            cost[j][i] -= min
        if min < sys.maxsize:
            LB += min
    return LB, cost



# return 最大成本的index
def Max_cost(cost):
    n = len(cost)
    m = 0
    max_i = 0
    max_j = 0
    for i in range(n):
        t = sorted(cost[i])
        if t[n-1] < 0: #此row已被刪除
            continue
        count = 0
        if t[0] < 0:
            while t[count] < 0:
                count+=1
        if count == n-1:
            m = t[count]
            max_i = i
            max_j = cost[i].index(t[count])
            break
        temp = cost[i].index(t[count+1])
        if cost[i][temp] < 0:
            continue
        if cost[i][temp] > m:
            m = cost[i][temp]
            max_i = i
            max_j = cost[i].index(t[count])
    return max_i, max_j, m

#設定不能再走的路
def clear(cost,in_i,in_j):
    n = len(cost)
    for i in range(n):
        for j in range(n):
            if cost[i][j] < 0:
                continue
            if i == in_i:
                cost[i][j] = -1
            if i == in_j and j == in_i:
                cost[i][j] = sys.maxsize
            if j == in_j:
                cost[i][j] = -1
    return cost

#建立樹 找可行解
def TSP(r, cost, lb, level):
    global min_LB
    if level == len(cost):
        if lb < min_LB:
            min_LB = lb
        return
    if lb > min_LB:
        return
    r.left = Tree()
    r.right = Tree()
    r.right.cost = copy.deepcopy(cost)
    in_i, in_j, m = Max_cost(cost)
    cost_t = copy.deepcopy(cost)
    r.left.f = in_i
    r.left.t = in_j
    cost_t = clear(cost_t,in_i,in_j)
    lb_t, cost_t= LowerBound(lb,cost_t)
    r.left.lb = lb_t
    r.left.cost = copy.deepcopy(cost_t)
    r.left.level = level + 1
    r.right.lb = lb + m
    r.right.level = level
    r.right.cost[in_i][in_j] = sys.maxsize
    lb_t, cost_t= LowerBound(r.right.lb,r.right.cost)
    r.right.cost = copy.deepcopy(cost_t)
    TSP(r.left, r.left.cost, r.left.lb, r.left.level)
    if r.right.level < len(cost) - 1:
        TSP(r.right, r.right.cost, r.right.lb, r.right.level)

#找最佳解
def check(r):
    global min_LB
    if r.lb > min_LB:
        return
    if r.level == len(r.cost):
        if r.lb > min_LB:
            return
        else:
            min_LB = r.lb
            return
    TSP(r, r.cost, r.lb,r.level)
    check(r.left)
    check(r.right)

#印出解答路徑
def vis(a, i):
    if a[i] == 0:
        print("0")
        return
    print(a[i]," -> ",end="")
    vis(a, a[i])

#建立解答路徑
def ans(path1, r):
    path = copy.deepcopy(path1)
    n = len(r.cost)
    visit = [None]*n
    i = 0
    while i < len(path):
        if path[i].f == None:
            del path[i]
        else:
            i += 1
    for i in range(len(path)):
        visit[path[i].f] = path[i].t
    print("0 -> ",end="")
    vis(visit, 0)
    print("cost : ", min_LB)

#掃描整棵樹
def all(r, path):
    global num
    if r == None:
        return
    if r.lb > min_LB or r.lb == None :
        return
    if r.level == len(r.cost):
        if r.lb > min_LB:
            return
        else:
            ans(path, path[0])
            num += 1
            return
    path.append(r.left)
    all(r.left, path)
    path.pop()
    path.append(r.right)
    all(r.right, path)
    path.pop()
    
file = open("test5.txt", "r")
n = int(file.readline())
cost = []

for i in range(n):
    cost.append([])
    t = file.readline().split()
    for j in range(n):
        cost[i].append(int(t[j]))

#將對角線設為最大值
for i in range(n):
    for j in range(n):
        if i == j:
            cost[j][i] = sys.maxsize
            break
root = Tree()
lb, cost_t = LowerBound(0, cost)
root.lb = lb
root.cost = copy.deepcopy(cost_t)
root.level = 0

TSP(root, cost_t, lb, 0)

path = []
all(root, path)
print("共有",num,"種最佳解")