answer1 = [(0, 255, 255), (145, 0, 145), (145, 255, 145), (182, 182, 255), (255, 108, 156), (0, 0, 1)]
answer2 = [(0, 19, 239), (253, 255, 98), (181, 56, 168), (0, 205, 255), (86, 73, 193), (0, 255, 41)]

one_two = input("1?2? ")
ans = []
for _ in range(6):
    x = input("? ")
    ans.append((int(x[0:2], 16), int(x[2:4], 16), int(x[4:6], 16)))


sa = []
if one_two == "1":
    for i in range(6):
        sa.append(abs(ans[i][0] - answer1[i][0]) + abs(ans[i][1] - answer1[i][1]) + abs(ans[i][2] - answer1[i][2]))

if one_two == "2":
    for i in range(6):
        sa.append(abs(ans[i][0] - answer2[i][0]) + abs(ans[i][1] - answer2[i][1]) + abs(ans[i][2] - answer2[i][2]))

print(f"{sum(sa)}, {100-sum(sa)/16777216*100}%")
print(f"点数の詳細{sa}")