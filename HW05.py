A = input("請輸入第一個字串 : ")
B = input("請輸入第二個字串 : ")

len_A = len(A) + 1
len_B = len(B) + 1
array = [[None] * (len_B) for i in range(len_A)]

for i in range(len_B):
    array[0][i] = 0
for i in range(len_A):
    array[i][0] = 0

for i in range(1, len_A):
    for j in range(1, len_B):
        if A[i - 1] == B[j - 1]:
            array[i][j] = array[i - 1][j - 1] + 1
        else:
            array[i][j] = max(array[i - 1][j], array[i][j - 1])

print('{:^5}'.format(" "), end="")
print('{:^5}'.format(" "), end="")
for j in range(len_B-1):
    print('{:^5}'.format(B[j]), end="")
print()
for i in range(len_A):
    if i == 0:
        print('{:^5}'.format(" "), end="")
    else:
        print('{:^5}'.format(A[i-1]), end="")
    for j in range(len_B):
        print('{:^5}'.format(array[i][j]), end="")
    print()

longest = array[len_A-1][len_B-1]
i = len_A-1
j = len_B-1
LCS = []
while len(LCS) < longest:
    if A[i-1] == B[j-1]:
        LCS.append(A[i-1])
        i -= 1
        j -= 1
    else:
        if array[i - 1][j] > array[i][j - 1]:
            i -= 1
        else:
            j -= 1

LCS.reverse()
print("LCS : ", end="")
for i in LCS:
    print(i,end="")
