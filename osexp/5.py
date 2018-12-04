# 资源：A, B, C
Available = [5, 5, 7]

# [pid, A, B, C]
Max = [[0, 7, 5, 3],
       [1, 3, 2, 2],
       [2, 9, 0, 2],
       [3, 2, 2, 2],
       [4, 7, 5, 5], ]

# 已获得资源向量表 [pid, A, B, C]
Allocation = [[0, 2, 0, 0],
              [1, 0, 0, 0],
              [2, 0, 0, 0],
              [3, 0, 0, 0],
              [4, 3, 2, 2], ]

# 还需要的资源向量表 [pid, A, B, C]
Need = [[0, 5, 5, 3],
        [1, 3, 2, 2],
        [2, 9, 0, 2],
        [3, 2, 2, 2],
        [4, 4, 3, 3], ]

Finish = [False, False, False, False, False]


def main():
    cmd = ''
    show("ava")
    show("max")
    show("alloc")
    show("need")
    while True:
        cmd = input('cmd:>> ').split(' ')
        # print(cmd)
        if cmd[0] == 'request' and len(cmd) == 5:
            if not check_input(cmd):  # 输入不正确
                continue

            pid = int(cmd[1])
            cmd[1] = int(cmd[1])
            cmd[2] = int(cmd[2])
            cmd[3] = int(cmd[3])
            cmd[4] = int(cmd[4])

            # 预分配资源
            for index in range(3):
                Allocation[pid][index + 1] += cmd[index + 2]
                Need[pid][index + 1] -= cmd[index + 2]
                Available[index] -= cmd[index + 2]

            # show("ava")
            # show("alloc")
            # show("need")
            safe = is_safe()
            if not safe:
                # 不安全，撤销分配
                for index in range(3):
                    Allocation[pid][index + 1] -= cmd[index + 2]
                    Need[pid][index + 1] += cmd[index + 2]
                    Available[index] += cmd[index + 2]
                print("not safe! can not continue...")
            else:
                print("safe, accept...")

        elif cmd[0] == 'show' and len(cmd) == 2:
            if cmd[1] == "all":
                show("ava")
                show("alloc")
                show("need")
            else:
                show(cmd[1])

        elif cmd[0] == "exit":
            return

        else:
            print("bad command!")


def check_input(input_li: list):
    p_exist = False
    find_p = None
    # 判断进程存在性
    for p in Need:
        if int(input_li[1]) == p[0]:
            find_p = p
            p_exist = True
    if p_exist == False:
        print("process do not exist!")
        return False

    # 判断申请的资源是否合法
    for index in range(2, 5):
        if int(input_li[index]) > find_p[index - 1]:
            print("more than process need!")
            return False
        elif int(input_li[index]) < 0:
            print("please input unsigned integer!")
            return False
        elif int(input_li[index]) > Available[index - 2]:
            print("don't have so much resource!")
            return False

    return True


def show(param: str):
    param = param
    if param == "ava":
        print("  {:^30}  ".format("Available"))
        print("  {:-^30}  ".format(''))
        print("  {:^8} | {:^8} | {:^8}  ".format("A", "B", "C"))
        print("  {:-^30}  ".format(''))
        print("  {:^8} | {:^8} | {:^8}  ".format(Available[0], Available[1], Available[2]))
        print("  {:-^30}  ".format(''))
        print()

    elif param == "max" or param == "need" or param == "alloc":
        if param == "max":
            table = Max
        elif param == "need":
            table = Need
        elif param == "alloc":
            table = Allocation

        print("  {:^41}  ".format(param))
        print("  {:-^41}  ".format(''))
        print("  {:^8} | {:^8} | {:^8} | {:^8}  ".format("pid", "A", "B", "C"))
        print("  {:-^41}  ".format(''))
        for each_p in table:
            print("  {:^8} | {:^8} | {:^8} | {:^8}  ".format(each_p[0], each_p[1], each_p[2], each_p[3]))
        print("  {:-^41}  ".format(''))
        print()

    else:
        print("bad command!")


def is_safe():
    p = []
    work = Available.copy()
    pcs = len(Allocation)
    res = len(Available)
    rd = 0
    global Finish
    Finish = [False, False, False, False, False]
    while rd < pcs:
        find = False
        for i in range(pcs):
            if Finish[i]:
                continue
            enough = True
            for j in range(res):
                if Need[i][j + 1] > work[j]:
                    enough = False
                    break

            if enough:
                print(i, "Finished")
                print(work)
                Finish[i] = True
                for j in range(res):
                    work[j] += Allocation[i][j + 1]
                p.append(i)
                rd += 1
                find = True
                break
        if not find and False in Finish:
            return False
    print(p)
    return True


# def is_safe():
#     l = 0
#     n = len(Available)
#     m = len(Allocation)
#     p = [-1, -1, -1, -1, -1]
#     Work = Available.copy()
#     global Finish
#     Finish = [False, False, False, False, False]
#     while l < m:        
#         init_i = l
#         print("第{}轮".format(l))
#         for i in range(m):
#             if Finish[i]:
#                 print("pid:{} finished".format(i))
#                 continue

#             enough = True
#             for j in range(n):
#                 if Need[i][j + 1] > Work[j]:
#                     print("need[{}][{}]={} > work[{}]={}".format(i,j+1,Need[i][j + 1], j, Work[j]))
#                     enough = False
#                     break

#             if enough:
#                 print("---------enough")
#                 Finish[i] = True
#                 for k in range(n):
#                     Work[k] += Allocation[i][k + 1]
#                 p[l] = i
#                 l += 1
#                 break
#             else:
#                 continue
#         print(l,init_i)
#         if l == init_i:
#             return False
#     print("安全序列：")
#     for each in p:
#         print("{}   ".format(each), end='')
#     return True


main()
