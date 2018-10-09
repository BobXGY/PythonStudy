# 小球移动一次的函数
def move(ball: list, lenth_of_line: int):
    if ball[0] == "right":
        if ball[1] == lenth_of_line:  # 到右边界
            ball[1] -= 1
            ball[0] = "left"
        else:
            ball[1] += 1
    else:
        if ball[1] == 0:  # 到左边界
            ball[1] += 1
            ball[0] = "right"
        else:
            ball[1] -= 1


# 碰撞检测
def meet(ball1: list, ball2: list):
    if ball1[1] == ball2[1]:
        return True
    else:
        return False


# 显示所有小球位置
def display_balls(ball_list: list):
    for ball in ball_list[:-1:]:
        print(ball[1], end=' ')
    print(ball_list[-1][1])


# 改变小球方向
def change_direction(ball: list):
    if ball[0] == "right":
        ball[0] = "left"
    else:
        ball[0] = "right"


if __name__ == '__main__':
    args_g1 = input().split(" ")  # 个数 线段长 时间
    args_g2 = input().split(" ")  # 初始时刻小球位置
    ball_list = list()
    line_lenth = int(args_g1[1])
    time = int(args_g1[2])
    for number in range(0, int(args_g1[0])):
        # 小球的格式： ball[direction: str, position: int]
        ball_list.append(["right", int(args_g2[number]), False])

    while True:
        if time == 0:
            break

        for aball in ball_list:  # 对所有小球的两两组合进行碰撞检测
            if aball[2]:  # 如果已经逆置方向则跳过
                aball[2] = False
                continue
            for bball in ball_list:
                if bball == aball:
                    continue
                if meet(aball, bball):
                    bball[2] = True  # 避免重复逆置方向的标记
                    change_direction(aball)
                    change_direction(bball)
                    break

        for ball in ball_list:  # 移动所有小球
            move(ball, line_lenth)

        time -= 1

    display_balls(ball_list)
