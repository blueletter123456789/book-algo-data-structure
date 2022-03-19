n = int(input())
red_points = sorted([list(map(int, input().split())) for _ in range(n)])
blue_points = sorted([list(map(int, input().split())) for _ in range(n)])
seen = set()
for i in range(n):
    idx = 0
    for j in range(n):
        if red_points[j][0] < blue_points[i][0]:
            idx += 1
        else:
            break
    max_y = -1
    for k in range(idx):
        if red_points[k][1] < blue_points[i][1] and k not in seen:
            if max_y == -1 or red_points[max_y][1] < red_points[k][1]:
                max_y = k
    if max_y >= 0:
        seen.add(max_y)
print(len(seen))
