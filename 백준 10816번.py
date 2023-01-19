import sys
input = sys.stdin.readline
num = int(input())
sanggeun_list = list(map(int,input().split()))
num_2 = int(input())
target_list = list(map(int,input().split()))
sanggeun_list.sort()
def binary_search(start,end,data,target):
    while start <= end:
        mid = (start + end)//2
        if data[mid] == target:
            return cnt.get(target)
        elif target > data[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0
cnt = {}
for i in sanggeun_list:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1
# print(cnt)
for i in target_list:
    print(binary_search(0,num-1,sanggeun_list,i),end=' ')