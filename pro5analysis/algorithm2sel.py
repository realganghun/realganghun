# 리스트 안에 들어 있는 자료를 오름차순 정렬

#1) 선택(selection) 정렬
# 방법1 : 이해 위주

def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort(a):
    result = []
    while a:
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)
    return result

d = [2, 4, 5, 1, 3]
# print(find_min_idx(d))
print(sel_sort(d))

# 방법 2 : 일반 알고리즘
def sel_sort2(a):
    n = len(a)
    for i in range(0, n - 1): # 0부터 n-2까지 반복
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i] #찾은 최소값을 i번 위치로 이동


d = [2, 7, 8, 1, 10, 9, 6, 3, 5, 4]

sel_sort2(d)
print(d)