import sys
sys.stdin = open("input.txt","r")

N = int(input())

meetings = [tuple(map(int,input().split())) for _ in range(N)]
meetings.sort(key=lambda x: x[0])
meetings.sort(key=lambda x: x[1])

cnt = 0
end_time = 0

for s, e in meetings:
    if s >= end_time:
        cnt += 1
        end_time = e

print(cnt)


